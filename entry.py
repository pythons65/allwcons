import os
import sys
import subprocess
from color import *
from userUtils import *
from import_file import import_file

def entries(console,commands):

    def importer(path, moduleName):
        p = console.getPath()
        filename = wconsBunddle(moduleName)
        mylib = import_file(os.path.join(p, filename))
        e = mylib.entries(console, commands)
        commands.addCommands(e[0])
        commands.modules.addModule(e[0], moduleName)
        if(len(e[1]) > 0):
            commands.setDobuleCommandDict(e[1])
        log("imported")




    cmd = {
        "exit()" :{
            "*":lambda path,args: console.breakLoop()
        },
        "cls": lambda path,args:clear(),
        "ls":{
            "*": lambda path,args:dirs(),
            "-r":lambda path,args: dirs(True),
            "${other}":lambda path,args: warn("only -r supported yet " + args + " not suporeted")
        },
        "cd":{
            "*": lambda path,args: warn("please provide path"),
            "${path}":lambda path,args: cd(args,console),
            "..": lambda path,args: cdBack(console)
        },
        "pwd": lambda path,args:log(console.getPath(),type="special"),
        "mkdir":{
            "*":lambda path,args: warn("pleae provide dir path"),
            "${folder}":lambda path,args:mkdir(args)
        },
        "rmdir":{
            "*":lambda path,args: warn("pleae provide dir path"),
            "${folder}":lambda path,args:rmdir(args)            
        },
        "isexist": {
            "*":lambda path,args: warn("pleae provide dir path"),
            "${path}":{
                "*": lambda path,args: warn("please provide check type"),
                "-dir":lambda path,args: dirExist(args["path"]),
                "-file":lambda path,args: fileExist(args["path"])
            }
        },
        #import should be in wcons extension file
        "import": {
            "*": lambda path,args:warn("please provide path"),
            "${path}": lambda path,args: importer(path,args)
        },
        "delete":{
            "*": lambda path,args:warn("please provide path"),
            "${path}": lambda path,args: commands.modules.delModule(args)
        }

    }
    newCmds = {
    "dir":"ls",
    "clear":"cls"
}

    return [cmd,newCmds]