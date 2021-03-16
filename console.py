from color import *
import colorama
from colorama import Style
colorama.init()

class Console:
    def __init__(self):
        self.__inputs = []
        self.__len = -1
        self.__breaker = True

    def addCommands(self,command):
        self.__Command = command

    def takeCommand(self, path, loop=False):
        print("\u001b[32m")
        self.__path = path
        if(loop):
            while self.__breaker:
                command = input(self.__path).rstrip()
                self.run(command)
                self.__inputs.append(command)
                self.__len += 1
        else:
            command = input(self.__path).rstrip()
            self.run(command)
            self.__inputs.append(command)
            self.__len += 1
        print(Style.RESET_ALL)
    
    def space(self):
        print("\n")
    def changePath(self,path):
        self.__path = path
    
    def getPath(self):
        return self.__path[:-1]

    def run(self,command):

        try:
            self.__Command.run(command, self.__path)
        except AttributeError as e:
            log(f"no Commands added or {e}",type="error")

    def breakLoop(self):
        self.__breaker = False
    def commandLast(self):
        return self.__inputs[self.__len]
    def commands(self):
        return self.__inputs
