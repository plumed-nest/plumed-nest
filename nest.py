#!/usr/bin/env python
# coding: utf-8

import yaml
import sys
import time
import getopt
import shutil
import re
import urllib.request
import zipfile
from contextlib import contextmanager
import os
import json
import pathlib
import subprocess
from PlumedToHTML import test_plumed, get_html, get_javascript, get_css 
from datetime import datetime
from pytz import timezone

if not (sys.version_info > (3, 0)):
   raise RuntimeError("We are using too many python 3 constructs, so this is only working with python 3")

class ChecksumError(Exception):
    """ Raised when a checksum is violated. """
    pass

def convert_date(date_str):
    objDate = datetime.strptime(date_str, '%Y-%m-%d')
    return datetime.strftime(objDate,'%d %b %Y')

def md5(path):
    """ Compute the MD5 hash of a path and return it as a string. """
    import hashlib
    if not isinstance(path,str):
        raise TypeError("path should be a string")
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
    md5 = hashlib.md5()
    with open(path, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()

def get_reference(doi,ref,ref_url):
    # initialize preprint
    prep = 0
    # retrieve citation from doi
    if(len(doi)>0):
      # check if unpublished/submitted
      if(doi.lower()=="unpublished" or doi.lower()=="submitted"): 
        ref=doi.lower()
      # get info from doi
      else:
        try:
          # get citation
          cit = subprocess.check_output('curl -LH "Accept: text/bibliography; style=science" \'http://dx.doi.org/'+doi+'\'', shell=True).decode('utf-8').strip()
          if("DOI Not Found" in cit): 
           ref="DOI not found"
          else:
           # get citation
           ref=cit[3:cit.find(", doi")]
           # and url
           ref_url="http://dx.doi.org/"+doi
           # check if bioRxiv/medRxiv
           if(doi.split('/')[0]=='10.1101'): prep = 1
           # check if Research Square
           if(doi.split('/')[0]=='10.21203'): prep = 1
        except:
          ref="DOI not found" 
    # arXiv and ChemRxiv
    if('arxiv' in ref_url.lower() or 'chemrxiv' in ref_url.lower()): prep = 1
    return ref,ref_url,prep
 
def get_short_name_ini(lname, length):
    if(len(lname)>length): sname = lname[0:length]+"..."
    else: sname = lname
    return sname

def get_short_name_end(lname, length):
    l=len(lname)
    if(l>length): sname = "..."+lname[l-length:l]
    else: sname = lname
    return sname

def plumed_format(source,tested,status,exe,actions,usejson=False,global_header=None,header=None):
    """ Format plumed input file.

    source: path to master input file
    tested: versions of plumed that were tested
    exe: executables that were used for testing
    global_header: header added to all the (recursively) converted files.
    run_header: header added only to the master file.

    """
    suffix="md"
    # list of generated files, returned
    lista=[]
    with open(source) as f:
        destination=source + "." + suffix
        lista.append(destination)
        with open(destination,"w") as o:
            if global_header:
                 print(global_header,file=o)
            print("**Source:** " + re.sub("^data/","",source)+"  ",file=o)
            if header:
                 print(header,file=o)
            # Read in the input file and get the rendered html
            lines = f.read()
            html = get_html( lines, source, os.path.basename(source), tested, status, exe, usejson=usejson, maxchecks=100, actions=actions )
            # make sure Jekyll does not interfere with format
            print("{% raw %}",file=o)
            print( html, file=o )
            print("{% endraw %}",file=o)
            # convert to set to remove duplicates
            return list(set(lista))

def add_readme(file, tested, success, exe, has_load, has_custom):
    with open("README.md","a") as o:
        badge = ''
        for i in range(len(tested)):
            if success[i]!="ignore":
                badge = badge + ' [![tested on ' + tested[i] + '](https://img.shields.io/badge/' + tested[i] + '-'
                if success[i]=="custom": # not used now 
                    badge = badge + 'custom-yellow.svg'
                elif success[i]==0: 
                    badge = badge + 'passing-green.svg'
                else:
                    badge = badge + 'failed-red.svg'
                badge = badge + ')](' + file + '.' +  exe[i] + '.stderr)'
        if has_load:
            badge += ' [![with LOAD](https://img.shields.io/badge/with-LOAD-yellow.svg)]({{ "/" | absolute_url }}badges)'
        if has_custom:
            badge += ' [![with custom code](https://img.shields.io/badge/with-custom_code-red.svg)]({{ "/" | absolute_url }}badges)'
        print("| [" + get_short_name_end(re.sub("^data/","",file), 50) + "](./"+file+".md"+") | " + badge + " |" + "  ", file=o)


@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)

def process_egg(path,action_counts,plumed_syntax,eggdb=None):

    if not eggdb:
        eggdb=sys.stdout

    with cd(path):
        # start timing
        start_time = time.perf_counter()
        # open file
        stram = open("nest.yml", "r")
        config=yaml.load(stram,Loader=yaml.BaseLoader)
        # check fields
        for field in ("url","pname","category","keyw","contributor","history"):
            if not field in config:
               raise RuntimeError(field+" not found")
        # check presence of either "doi" or ("ref" and "ref_url")
        if("doi" not in config and ("ref" not in config or "ref_url" not in config)):
          raise RuntimeError(" doi or ref/ref_url not found")
        # initialize some fields
        if("doi" not in config):
          config["doi"]=""
        if("ref" not in config or "ref_url" not in config):
          config["ref"]=""
          config["ref_url"]="" 
        print(path,config)

        # allow using a dictionary. We might enforce a dictionary here if we prefer this syntax.
        if isinstance(config["history"],dict):
           h=[]
           for k in sorted(config["history"]):
              h.append([k,config["history"][k]])
           config["history"]=h

        #if re.match("^.*\.zip$",config["url"]):
        if os.path.exists("download"):
           shutil.rmtree("download")
        os.mkdir("download")
        # try to download
        try:
         urllib.request.urlretrieve(config["url"], 'file.zip')
        except urllib.error.URLError:
         return
        if "md5" in config:
            md5_=md5("file.zip")
            if md5_ != config["md5"] :
               raise ChecksumError("md5 not matching " + md5_)
        # try to open the zip file
        try:
          zf = zipfile.ZipFile("file.zip", "r")
        except zipfile.BadZipFile:
          return
        zf_namelist = zf.namelist()
        root=list(set([ x.split("/")[0] for x in zf_namelist]))
        # there is a main root directory
        if(len(root)==1 and len(zf_namelist)!=1): root="download/" + root[0]
        # there is not (or special case of one single file)
        else:        root="download/"
        zf.extractall(path="download")
        if os.path.exists("data"):
           shutil.rmtree("data")
        shutil.move(root,"data")
        #else:
        #    raise RuntimeError("cannot interpret url " + config["url"])

        if not "plumed_input" in config:
            # discover path relative to data dir
            with cd("data"):
                config["plumed_input"]=sorted(pathlib.Path('.').glob('**/plumed*.dat'))
                config["plumed_input"]=[ {"path":str(v)} for v in config["plumed_input"]]
        else:
            conf=config["plumed_input"]
            for k in range(len(conf)):
                if not isinstance(conf[k],dict):
                    conf[k]={"path":conf[k]}

        # take maximum number of input files
        maxinp = min(20, len(config["plumed_input"]))
        config["plumed_input"] = config["plumed_input"][0:maxinp]

        # prepend data to all paths
        for f in config["plumed_input"]:
            f["path"]="data/" + f["path"]

        egg_id=path[5:7] + "." + path[8:11]
        global_header="**Project ID:** [plumID:" + egg_id+"]({{ '/' | absolute_url }}" + path + ")  "

        with open("badge.svg","w") as badge:
            print("<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"120\" height=\"20\">", file=badge)
            print("<linearGradient id=\"a\" x2=\"0\" y2=\"100%\">", file=badge)
            print("<stop offset=\"0\" stop-color=\"#bbb\" stop-opacity=\".1\"/>", file=badge)
            print("<stop offset=\"1\" stop-opacity=\".1\"/></linearGradient>", file=badge)
            print("<rect rx=\"3\" width=\"120\" height=\"20\" fill=\"#555\"/>", file=badge)
            print("<rect rx=\"3\" x=\"67\" width=\"53\" height=\"20\" fill=\"#155799\"/>", file=badge)
            print("<path fill=\"#155799\" d=\"M67 0h4v20h-4z\"/>", file=badge)
            print("<rect rx=\"3\" width=\"120\" height=\"20\" fill=\"url(#a)\"/>", file=badge)
            print("<g fill=\"#fff\" text-anchor=\"middle\" font-family=\"DejaVu Sans,Verdana,Geneva,sans-serif\" font-size=\"11\">", file=badge)
            print("<text x=\"34.5\" y=\"15\" fill=\"#010101\" fill-opacity=\".3\">plumID</text>", file=badge)
            print("<text x=\"34.5\" y=\"14\">plumID</text>", file=badge)
            print("<text x=\"92.5\" y=\"15\" fill=\"#010101\" fill-opacity=\".3\">"+egg_id+"</text>", file=badge)
            print("<text x=\"92.5\" y=\"14\">"+egg_id+"</text></g></svg>", file=badge)

        with open("README.md","w") as o:
            print(global_header, file=o)
            print("**Name:** ",config["pname"]+"  ", file=o)
            browse_archive=""
            if re.match("https://github\.com/[^/]+/[^/]+/archive/[^/]+\.zip\Z",config["url"]):
                browse_archive=" [(browse)](" + (
                    re.sub("\.zip\Z","",re.sub("/archive/","/tree/",config["url"]))
                )+ ")"
            print("**Archive:** [",config["url"]+"]("+config["url"]+")" +
                  browse_archive +"  ", file=o)
            if "md5" in config:
                print("**Checksum (md5):**",config["md5"]+"  ", file=o)
            print("**Category:** ",config["category"]+"  ", file=o)
            print("**Keywords:** ",config["keyw"]+"  ", file=o)
            if "plumed_version" in config:
                print("**PLUMED version:** ",config["plumed_version"]+"  ", file=o)
            print("**Contributor:** ",config["contributor"]+"  ", file=o)
            print("**Submitted on:** "+convert_date(config["history"][0][0])+"  ", file=o)
            if(len(config["history"])>1):
              print("**Last revised:** "+convert_date(config["history"][-1][0])+"  ", file=o)
            # retrieve reference,url, and preprint flag
            ref,ref_url,prep = get_reference(config["doi"],config["ref"],config["ref_url"])
            if(ref=="unpublished" or ref=="submitted" or ref=="DOI not found"):
              print("**Publication:** " + ref + "  ", file=o)
            else:
              print("**Publication:** [" + ref + "]("+ref_url+")  ", file=o)
            print("  ", file=o)
            print("**PLUMED input files**  ", file=o)
            print("  ", file=o)
            print("| File     | Compatible with |  ", file=o) 
            print("|:--------:|:--------:|  ", file=o)

        # count number of failing tests
        nfail=0; nfailm=0
        actions = set({})
        for file in config["plumed_input"]:
            print("PROCESSING FILE NAMED " + str(file["path"]) )

            if "natoms" in file:
                natoms = int(file["natoms"])
            elif "natoms" in config:
                natoms = int(config["natoms"])
            else:
                natoms = 100000

            if "nreplicas" in file:
                nreplicas = int(file["nreplicas"])
            elif "nreplicas" in config:
                nreplicas = int(config["nreplicas"])
            else:
                nreplicas = 0 # 0 means do not use mpiexec
            
            # If the number of replicas is not one or the number of atoms is not 1000000 then put that information in the input file
            if natoms!=100000 or nreplicas!=0 : 
               ifile = open( file["path"] )
               inp = ifile.read()
               ifile.close()
               ofile = open( file["path"], "w+" )
               if natoms!=100000 and nreplicas!=0 : ofile.write("#SETTINGS NREPLICAS=" + str(nreplicas) + " NATOMS=" + str(natoms) + "\n" )
               elif natoms!=100000 : ofile.write("#SETTINGS NATOMS=" + str(natoms) + "\n" )
               elif nreplicas!=0 : ofile.write("#SETTINGS NREPLICAS=" + str(nreplicas) + "\n" )
               ofile.write( inp )
               ofile.close()

            if "plumed_version" in file:
                plumed_version=file["plumed_version"]
            elif "plumed_version" in config:
                plumed_version=config["plumed_version"]
            else:
                plumed_version="not specified"

            header="**Originally used with PLUMED version:** " + plumed_version + "  \n"
            # output and error files for stable version
            header+= "**Stable:** [zipped raw stdout]("+ re.sub(".*/","",file["path"]) +".plumed.stdout.txt.zip) - "
            header+= "[zipped raw stderr]("+ re.sub(".*/","",file["path"]) +".plumed.stderr.txt.zip) - "
            header+= "[stderr]("+ re.sub(".*/","",file["path"]) +".plumed.stderr)  \n"
            # output and error files for master version
            header+= "**Master:** [zipped raw stdout]("+ re.sub(".*/","",file["path"]) +".plumed_master.stdout.txt.zip) - "
            header+= "[zipped raw stderr]("+ re.sub(".*/","",file["path"]) +".plumed_master.stderr.txt.zip) - "
            header+= "[stderr]("+ re.sub(".*/","",file["path"]) +".plumed_master.stderr)  \n"

# in principle returns the list of produced files, not used yet:
            has_custom = re.match(".*-mod",plumed_version)

            # Get the directory we are working in
            directory = os.path.dirname(file["path"])
            if not pathlib.Path(f"./{directory}/plumedtohtml.js").exists() :
               # Print the js for plumedToHTML to a file
               with open(f"{directory}/plumedtohtml.js", "w+") as jf : jf.write( get_javascript() )
            if not pathlib.Path(f"./{directory}/plumedtohtml.css").exists() :
               # Print the css for plumedToHTML to a file
               with open(f"{directory}/plumedtohtml.css", "w+") as jf : jf.write( get_css() )
            
            success=test_plumed("plumed",file["path"],header=global_header)
            if(success!=0 and success!="custom"): nfail+=1
            plumed_file = os.path.basename(file["path"])
            success_master=test_plumed("plumed_master",file["path"],header=global_header, printjson=True )
            if(success_master!=0 and success_master!="custom"): nfailm+=1
            # Find the stable version 
            stable_version=subprocess.check_output('plumed info --version', shell=True).decode('utf-8').strip()
            if plumed_version != "not specified":
                if int(re.sub("[^0-9].*","",re.sub("^2\\.","",stable_version))) < int(re.sub("[^0-9].*","",re.sub("^2\\.","",plumed_version))):
                   success="ignore"
            # Generate the plumed input 
            plumed_format(file["path"], ("v"+ stable_version,"master"), (success,success_master), ("plumed","plumed_master"), actions, usejson=(not success_master), global_header=global_header,header=header)
            add_readme(file["path"], ("v"+ stable_version,"master"), (success,success_master),("plumed","plumed_master"),("LOAD" in actions),has_custom)

        # print instructions, if present
        with open("README.md","a") as o:
             print("  ", file=o)
             currentDT = datetime.now(timezone('CET'))
             print("**Last tested:**  "+currentDT.strftime("%d %b %Y, %H:%M:%S"), file=o)
             print("  ", file=o)
             print("**Project description and instructions**  ", file=o)
             try:
               print(config["instructions"], file=o)
             except KeyError:
               print("*Description and instructions not provided*  ",file=o)
             print("  ", file=o)
             print("**Submission history**  ", file=o)
             for i,h in enumerate(config["history"]): 
                 print("**[v"+str(i+1)+"]** "+convert_date(h[0])+": "+h[1]+"  ", file=o)
             if "acknowledgement" in config:
                print("  ", file=o)
                print("**Acknowledgement**  ", file=o)
                print(config["acknowledgement"], file=o)
             print("  ", file=o)   
             print("**Badge**  ", file=o)
             print("Click on the image below and get the code to add the badge to your website!  ", file=o)
             print("<img src=\"./badge.svg\" alt=\"plumeDnest:" + egg_id + "\" id=\"myBtn\" class=\"badge\">", file=o)
             print("<div id=\"myModal\" class=\"modal\">", file=o)
             print("  <div class=\"modal-content\">", file=o)
             print("    <span class=\"close\">&times;</span>", file=o)
             print("    Markdown<pre>[![plumID:" + egg_id + "](https://www.plumed-nest.org/eggs/" + path[5:7] + "/" + path[8:11] + "/badge.svg)](https://www.plumed-nest.org/eggs/" + path[5:7] + "/" + path[8:11] + "/)</pre>", file=o)
             print("    HTML<pre>&lt;a href=\"https://www.plumed-nest.org/eggs/" + path[5:7] + "/" + path[8:11] + "/\"&gt;&lt;img src=\"https://www.plumed-nest.org/eggs/" + path[5:7] + "/" + path[8:11] + "/badge.svg\" alt=\"plumID:" + egg_id + "\"&gt;&lt;/a&gt;</pre>", file=o)
             print("  </div>", file=o)
             print("</div>", file=o)

# quote around id is required otherwise Jekyll thinks it is a number
        print("- id: '" + egg_id + "'",file=eggdb)
        print("  name: '" + config["pname"] + "'",file=eggdb)
        print("  shortname: '" + get_short_name_ini(config["pname"],15) +"'",file=eggdb)
        print("  category: " + config["category"],file=eggdb)
        print("  keywords: " + config["keyw"],file=eggdb)
        print("  shortkeywords: " + get_short_name_ini(config["keyw"],25),file=eggdb)
        print("  contributor: " + config["contributor"],file=eggdb)
        print("  doi: " + config["doi"],file=eggdb)
        print("  path: " + path,file=eggdb)
        print("  reference: '" + ref +"'",file=eggdb)
        print("  ref_url: '" + ref_url +"'",file=eggdb)
        print("  ninputs: " + str(len(config["plumed_input"])),file=eggdb)
        print("  nfail: " + str(nfail),file=eggdb)
        print("  nfailm: " + str(nfailm),file=eggdb)
        print("  preprint: " + str(prep),file=eggdb)
        modules = set()
        for a in actions :
            if a in plumed_syntax.keys() :
               try :
                 modules.add( plumed_syntax[a]["module"] )
               except : 
                 raise Exception("could not find module for action " + a)
            if a in action_counts.keys() : action_counts[a] += 1
        astr = ' '.join(actions)
        print("  actions: " + astr,file=eggdb)
        modstr = ' '.join(modules)
        print("  modules: " + modstr, file=eggdb)
        # end timing
        end_time = time.perf_counter()
        # store time
        print("  time: " + str(end_time-start_time), file=eggdb)
    eggdb.flush()

if __name__ == "__main__":
    nreplicas, replica, argv = 1, 0, sys.argv[1:] 
    try: 
        opts, args = getopt.getopt(argv,"hn:r:",["nreplicas=","replica="])
    except: 
       print('nest.py -n <nreplicas> -r <replica number>')

    for opt, arg in opts:
       if opt in ['-h'] :
          print('nest.py -n <nreplicas> -r <replica number>')
          sys.exit()
       elif opt in ["-n", "--nreplicas"]:
          nreplicas = int(arg)
       elif opt in ["-r", "--replica"]:
          replica = int(arg)
    print("RUNNING", nreplicas, "REPLICAS. THIS IS REPLICA", replica )
    # write plumed version to file
    stable_version=subprocess.check_output('plumed info --version', shell=True).decode('utf-8').strip() 
    f=open("_data/plumed.yml","w")
    f.write("stable: v%s" % str(stable_version))
    f.close()
    # Get list of plumed actions from syntax file
    cmd = ['plumed_master', 'info', '--root']
    plumed_info = subprocess.run(cmd, capture_output=True, text=True )
    keyfile = plumed_info.stdout.strip() + "/json/syntax.json"
    with open(keyfile) as f :
        try:
           plumed_syntax = json.load(f)
        except ValueError as ve:
           raise InvalidJSONError(ve)
    # Make a dictionary to hold all the actions
    action_counts = {} 
    for key in plumed_syntax :
        if key=="vimlink" or key=="replicalink" or key=="groups" : continue
        action_counts[key] = 0
    # loop over lesson for this replica
    with open("_data/eggs" + str(replica) + ".yml","w") as eggdb:
        print("# file containing egg database.",file=eggdb)

        # list of paths for this replica - not ordered
        pathlist = [line.strip() for line in open("pathlist"+str(replica), 'r')]

        # Reduce the eggs by reading in the eggs to use from a file -- used for testing
        if os.path.exists("selected_eggs.dat") :
           pathlist = []
           with open("selected_eggs.dat", "r") as file:
              for readline in file : pathlist.append( pathlib.Path( './' + readline.strip() ) )
        # cycle on ordered list
        for path in sorted(pathlist, reverse=True, key=lambda m: str(m)):
            print("### PROCESSING EGG AT PATH " + str(path) ) 
            # process egg
            process_egg(re.sub("nest.yml$","",str(path)),action_counts,plumed_syntax,eggdb)
    # output yaml file with action counts
    action_list = [] 
    for key, value in action_counts.items() : action_list.append( {'name': key, 'number': value } )
    cfilename = "_data/actioncount" + str(replica) + ".yml"
    with open(cfilename, 'w' ) as file : 
        yaml.safe_dump(action_list, file)

