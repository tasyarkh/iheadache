import os

def clr():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')