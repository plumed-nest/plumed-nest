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
                        endplumed=True
                    elif len(words)>0:
                        action=words[0]
                if action=="__FILL__":
                    action=""
                if len(action)>0 and not continuation:
                    action_url='<a href="path/to/' + action + '.html" style="color:green">' + action + '</a>'
                    line=re.sub(action,action_url,line)
                if len(words)>0 and words[-1]=="...":
                    continuation=True
                if continuation and words[0]=="...":
                    continuation=False
                line=re.sub("(#.*$)","<span style=\"color:blue\">\\1</span>",line)
                if(endplumed):
                    line=re.sub("(^.*$)","<span style=\"color:blue\">\\1</span>",line)
                print(line + '<br>',file=o)


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
        config=yaml.load(stram)
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
        for file in config["plumed_input"]:
            plumed_format(file,file + ".html")



