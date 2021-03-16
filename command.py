from color import *
from utils import *
from import_file import import_file
from module import Modules


class Command:
    def __init__(self,c=None):
        self.__commands = {}
        self.__doubleCmd  = {}
        self.console = c
        self.modules = Modules(self)

    def addCommands(self,params):
        self.__commands = {**self.__commands, **params}

    def delete(self, key):
        del self.__commands[key]
    def run(self,command1,path):
        splited_command = command1.split(" ")
        command = splited_command[0]
        if(command in self.__commands):
            c = self.__commands[command]
            if(isinstance(c, dict)):
                extractor(self,self.__commands,splited_command,path,{})
            
            self.checkRun(c,path,{})
        elif command in self.__doubleCmd.keys():
            if self.console:
                joinedCmd = self.__doubleCmd[command]
                if(len(splited_command[1:]) > 0):
                    self.console.run(joinedCmd + " " + " ".join(splited_command[1:]))
                else:
                    self.console.run(joinedCmd)

        else:
            log("command not found",type="error")
    def checkRun(self, c, path,historyArgs):
        if(callable(c)):
            return c(path,historyArgs)

        elif(isinstance(c, str)):
            log(c)
    def setDoubleCommand(self, newCmd, oldCmd):
        if(oldCmd in self.__commands.keys()):
            self.__doubleCmd = {newCmd:oldCmd,**self.__doubleCmd}
        else:
            log(f"no command name {oldCmd} exists",type="error")

    def setDobuleCommandDict(self,dictCmd):

        for i in dictCmd.keys():
            self.setDoubleCommand(i,dictCmd[i])

    def changeConsole(self,c):
        self.console = c


            