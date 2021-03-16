import colorama
colorama.init()

COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

def error(error):
    r = colorText(f"[[red]]{error}[[green]]")
    print(r)

def warn(warning):
    r = colorText(f"[[yellow]]{warning}[[green]]")
    print(r)

def simple(text):
    r = colorText(f"[[green]]{text}[[green]]")
    print(r)

def special(text):
    r = colorText(f"[[cyan]]{text}[[green]]")
    print(r)

def log(text,type="simple"):
    if(type == "simple"):
        simple(text)
    elif(type == "error"):
        error(text)
    elif(type == "warn"):
        warn(text)
    elif(type == "special"):
        special(text)
        

