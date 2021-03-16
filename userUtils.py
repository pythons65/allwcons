import os
from os import name
import sys
from os import system
import subprocess
from color import *
from userUtils import *
 
import json


def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def mkdir(path):
    os.system(f"mkdir {path}")

def rmdir(path):
    os.system(f"rmdir {path}")

def dirExist(path):
    log(os.path.isdir(path))

def fileExist(path):
    log(os.path.isfile(path))

def cmdRunner(cmd):
    if name == 'nt': 
        _ = system(cmd) 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system(cmd)




def cd(path,c):
    try:
        path1 = os.path.join(os.getcwd(),path)
        os.chdir(path1)
        c.changePath(path1+">")
    except FileNotFoundError:
        error("filenot found")

def cdBack(c):
    parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
    os.chdir(parent_path)
    c.changePath(parent_path + ">")

def dirR(path,space=""):
  current_path = path
  list_dir = os.listdir(path)
  if(len(list_dir) == 0):
    return
  for content in list_dir:
    os.chdir(path)
    if os.path.isdir(content):
      log(space +"+ "+content)
      new_path = os.path.join(path,content)
      new_space =space +  "   "
      dirR(new_path,new_space)
    elif os.path.isfile(content):
      log(space +"-- "+content)
  os.chdir(current_path)

def dirs(recursive=False):
    if not recursive:
        #window
        if name == 'nt': 
            _ = os.system('dir') 
    
        # for mac and linux(here, os.name is 'posix') 
        else: 
            _ = os.system('ls')
    elif recursive:
        dirR(os.getcwd())



def loadJson(file):
  with open(file,"r") as f:
    w = f.read()
    res = json.loads(w)
    return res

def wconsBunddle(moduleName):
  filePath = os.path.join(moduleName + ".wcons")
  moduleJson = loadJson(filePath)
  return moduleJson["filename"]


