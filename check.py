import os
import sys
import subprocess
from color import *
from userUtils import *

def entries(console,commands):

    cmd = {

       "check": lambda path,args:log("ok")
       }
    return [cmd,{"check1":"check"}]