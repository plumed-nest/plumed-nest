#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function

import yaml
import sys
import re
import urllib.request
import zipfile
from contextlib import contextmanager
import os
import pathlib
import subprocess

def plumed_format(source,destination):
    with open(source) as f:
        with open(destination,"w") as o:
            lines = f.read().splitlines()
            continuation=False
            action=""
            endplumed=False
            for line in lines:
                words=re.sub("#.*","",line).split()
                if not endplumed and not continuation:
                    if len(words)>1 and re.match("^.*:$",words[0]):
                        action=words[1]
                    elif len(words)>0 and words[0]=="ENDPLUMED":
                        print("````",file=o)
                        endplumed=True
                    elif len(words)>0:
                        action=words[0]
                if len(action)>0 and not continuation:
                    und_action = ''
                    for ch in action:
                        und_action = und_action + '_' + ch
                    action_url="[" + action + "](https://plumed.github.io/doc-master/user-doc/html/" + und_action.lower() + ".html)"
                    line=re.sub(action,action_url,line)
                if len(words)>0 and words[-1]=="...":
                    continuation=True
                if continuation and words[0]=="...":
                    continuation=False
                line=re.sub("(#.*$)","`\\1`",line)
# "  " is newline in markdown
                print(line + "  " ,file=o)
            if(endplumed):
                print("````",file=o)

def plumed_input_test(source):
    child = subprocess.Popen(['plumed', 'driver', '--natoms', '100000', '--parse-only', '--kt', '2.49', '--plumed', source], stdout=subprocess.PIPE, stderr=subprocess.STDOUT) 
    stdout,stderr = child.communicate()
    rc = child.returncode
    return rc

def add_readme(file, success):
    with open("README.md","a") as o:
        badge = ''
        if success==0: 
            badge = badge + '[![Github Releases](https://img.shields.io/github/release/plumed/plumed2.svg)](https://github.com/plumed/plumed2/releases)'
        print("| [" + file + "](./"+file+".md"+") | | " + badge + " |" + "  ", file=o)


@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)

for path in pathlib.Path('.').glob('*/nest.yml'):

    path=re.sub("nest.yml$","",str(path))

    with cd(path):

        stram = open("nest.yml", "r")
        config=yaml.load(stram,Loader=yaml.BaseLoader)
        if not "url" in config:
            raise RuntimeError("url not found")
        print(config)

        if re.match("^.*\.zip$",config["url"]):
            urllib.request.urlretrieve(config["url"], 'file.zip')
            zf = zipfile.ZipFile("file.zip", "r")
            root=zf.namelist()[0]
            zf.extractall()
        else:
            raise RuntimeError("cannot interpret url " + config["url"])

        if not "plumed_input" in config:
            config["plumed_input"]=sorted(pathlib.Path('.').glob('**/plumed*.dat'))
            config["plumed_input"]=[str(v) for v in config["plumed_input"]]
        print(config)

        with open("README.md","w") as o:
            print("| file     | original plumed relase | compatible with latest relase |  ", file=o) 
            print("|:--------:|:---------:|:--------:|  ", file=o)

        for file in config["plumed_input"]:
            plumed_format(file,file + ".md")
            success=plumed_input_test(file)
            add_readme(file, success)



