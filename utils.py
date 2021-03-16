from os import system, name 
from color import log


def extractor(this,commands,entry,path,historyArgs):
    if(len(entry) == 0):
        this.checkRun(commands["*"],path,historyArgs)
        return
    try:
        c = commands[entry[0]]

        if(isinstance(c, dict)):
            entry.pop(0)
            extractor(this,c,entry,path,historyArgs)
        else:
            this.checkRun(c,path,historyArgs)
    except KeyError as e:
        template = sFinder(commands)
        # "$" in commands
        if(template != None):  
            if(template[0] == True):
                key = "${"+template[1]+"}"

                c = commands[key]
                if(isinstance(c, dict)):
                    newArgs = {template[1]:entry[0]}
                    entry.pop(0)
                    historyArgs = {**historyArgs,**newArgs}
                    extractor(this,c,entry,path,historyArgs)
                if(callable(c)):
                    if(len(entry) > 1):
                        new_entry = entry
                        new_entry = " ".join(new_entry)
                        return c(path,new_entry)
                    return c(path,entry[0])
                elif(isinstance(c, str)):
                    log(c)

def sFinder(dicts):
    for i in dicts:
        check = templater(i)
        if(check[0]):
            return check

def templater(template):
    try:
        start = template[0]
        dillL = template[1]
        dillR = template[-1]
        if(start == "$" and dillL == "{" and dillR == "}"):
            return [True,template[2:-1]]
        else:
            return [False]
    except:
        return [False]


