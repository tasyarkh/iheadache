from colorama import init, Fore
from sys import stdout
import time
from view.clear import clr
from view.colors import Colors

FG = Fore.GREEN
FR = Fore.RED
FW = Fore.WHITE
FY = Fore.YELLOW
FC = Fore.CYAN
init(autoreset=True)

def banners():
    clr()
    stdout.write("                                                                                         \n")
    stdout.write(Colors.RED + "  ____  _                                   \n")
    stdout.write(Colors.RED + " |  _ \\(_) __ _  __ _ _ __   ___  ___  __ _ \n")
    stdout.write(Colors.RED + " | | | | |/ _` |/ _` | '_ \\ / _ \\/ __|/ _` |\n")
    stdout.write(Colors.RED + " | |_| | | (_| | (_| | | | | (_) \\__ \\ (_| |\n")
    stdout.write(Colors.RED + " |____/|_|\\__,_|\\__, |_| |_|\\___/|___/\\__,_|\n")
    stdout.write(Colors.GREEN + "                 |___/                        _      \n")          
    stdout.write(Colors.GREEN + " | |/ /___ _ __   ___ _ __ __ ___      ____ _| |_ __ _ _ __  \n")
    stdout.write(Colors.GREEN + " | ' // _ \\ '_ \\ / _ \\ '__/ _` \\ \\ /\\ / / _` | __/ _` | '_ \\ \n")
    stdout.write(Colors.GREEN + " | . \\  __/ |_) |  __/ | | (_| |\\ V  V / (_| | || (_| | | | |\n")
    stdout.write(Colors.GREEN + " |_|\\_\\___| .__/ \\___|_|  \\__,_| \\_/\\_/ \\__,_|\\__\\__,_|_| |_|\n")
    stdout.write(Colors.GREEN + "          |_|                                                \n")
    stdout.write(Fore.YELLOW + "═════════════╦═════════════════════════════════╦══════════════════════════════\n")
    stdout.write(Fore.YELLOW + "╔════════════╩═════════════════════════════════╩═════════════════════════════╗\n")
    stdout.write(Fore.YELLOW + "║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"Create By          "+Fore.RED+"    |"+Fore.WHITE+"   KELOMPOK 4                                    "+Fore.YELLOW+"║\n")
    stdout.write(Fore.YELLOW + "╔════════════════════════════════════════════════════════════════════════════╝\n")
    stdout.write(Fore.YELLOW + "║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"Dosen DP     "+Fore.RED+"                 |"+Fore.WHITE+"   Bapak Gofar                            "+Fore.YELLOW+"║\n")
    stdout.write(Fore.YELLOW + "╚════════════════════════════════════════════════════════════════════════════╝\n")