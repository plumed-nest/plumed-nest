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
            comment=False
            action=""
            endplumed=False
            for line in lines:
                words=line.split()
                #words=re.sub("#.*","",line).split()
                if not endplumed and not continuation:
                    if len(words)>1 and re.match("^.*:$",words[0]):
                        action=words[1]
                    elif len(words)>0 and words[0]=="ENDPLUMED":
                        print("````",file=o)
                        endplumed=True
                    elif len(words)>0 and not re.match("#",words[0]):
                        action=words[0]
                    elif len(words)>0 and re.match("#",words[0]):
                        comment = True
                if len(action)>0 and not continuation and not comment:
                    und_action = ''
                    for ch in action:
                        und_action = und_action + '_' + ch
                    action_url="[" + action + "](https://plumed.github.io/doc-master/user-doc/html/" + und_action.lower() + ".html)"
                    line=re.sub(action,action_url,line)
                if len(words)>0 and words[-1]=="...":
                    continuation=True
                if len(words)>0 and continuation and words[0]=="...":
                    continuation=False
                if comment:
                    comment=False
                line=re.sub("(#.*$)","`\\1`",line)
# "  " is newline in markdown
                print(line + "  " ,file=o)
            if(endplumed):
                print("````",file=o)

def plumed_input_test(source):
    run_folder = pathlib.PurePosixPath(source).parent
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

with open("list.md","w") as o:
    print("Browse the nest", file=o)
    print("-----------------------------", file=o)
    print("Here is a list of the projects already deposited on PLUMED-NEST", file=o)
    print(" ", file=o)
    print("| project     | category | keywords | author(s) |", file=o) 
    print("|:--------:|:---------:|:---------:|:---------:|",   file=o)

for path in pathlib.Path('.').glob('*/nest.yml'):

    path=re.sub("nest.yml$","",str(path))

    with cd(path):

        stram = open("nest.yml", "r")
        config=yaml.load(stram,Loader=yaml.BaseLoader)
        # check fields
        for field in ("url","pname","category","keyw","auths","cit","cit_url"):
            if not field in config:
               raise RuntimeError(field+" not found")
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
            print("**Project name:** ",config["pname"]+"  ", file=o)
            print("**Archive:** [",config["url"]+"]("+config["url"]+")  ", file=o)
            print("**Category:** ",config["category"]+"  ", file=o)
            print("**Keywords:** ",config["keyw"]+"  ", file=o)
            print("**Authors:** ",config["auths"]+"  ", file=o)
            print("**Publication:** ["+config["cit"]+"]("+config["cit_url"]+")"+"  ", file=o)
            print("**PLUMED input files:**  ", file=o)
            print("  ", file=o)
            print("| file     | original PLUMED release | compatible with |  ", file=o) 
            print("|:--------:|:---------:|:--------:|  ", file=o)

        for file in config["plumed_input"]:
            plumed_format(file,file + ".md")
            success=plumed_input_test(file)
            add_readme(file, success)

        # print instructions, if present
        with open("README.md","a") as o:
             print("  ", file=o)
             print("**Project description and instructions**  ", file=o)
             try:
               ifile = open("Instructions.md","r")
               print(ifile.read(), file=o)
               ifile.close()
             except FileNotFoundError:
               print("*Description and instructions not provided*  ",file=o)

        # add to list of projects
        with open("../list.md","a") as o:
            text='| [' + config["pname"] + ']('+path+') | '+config["category"]+ ' | ' + config["keyw"] +' |  ' + config["auths"] + '|' 
            print(text, file=o)

