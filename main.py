from console import Console
import os
import sys
import subprocess
from command import Command
from utils import *
from color import *
from userUtils import *
from entry import entries



c = Console()
cmd = Command(c)


cmd.addCommands(entries(c,cmd)[0])
cmd.setDobuleCommandDict(entries(c,cmd)[1])


c.addCommands(cmd)
c.takeCommand(f"{os.getcwd()}>",loop=True)

