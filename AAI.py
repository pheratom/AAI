import os
import time
import colorama
import sys
from colorama import Fore, Back, Style
try:
    from appInstaller import Install
    from workModes import *
    from appList import printAppList as printAppList
except ModuleNotFoundError:
    colorama.init(autoreset = True)
    print(f"{Fore.RED}You did't installed requirement packages.")
    answer = input(f"Install packages? (y/n) ")
    if answer == 'y':
        os.system('sudo apt install python3 python3-pip gnupg curl -y')
        os.system('python3 -m pip install wget && python3 -m pip install colorama')
        print(f"{Fore.RED}Restart app.")
        sys.exit()
    elif answer == 'n':
        print(f"Ok, exitting...")
        sys.exit()
    else:
        print("You need to type 'y' or 'n'. Nothing else!")
        sys.exit()
else:
    from appInstaller import Install
    from workModes import *
    from appList import printAppList as printAppList
colorama.init(autoreset = True)
if __name__ == '__main__':
    print(Fore.GREEN + '''
                     _____        __   ____  
     /\        /\   |_   _|      /_ | |___ \ 
    /  \      /  \    | |   __   _| |   __) |
   / /\ \    / /\ \   | |   \ \ / / |  |__ < 
  / ____ \  / ____ \ _| |_   \ V /| |_ ___) |
 /_/    \_\/_/    \_\_____|   \_(_)_(_)____/ ''') #https://www.fontchanger.net/ascii-text.html Font - Big
    while True:
        printAppList()
        try:
            mode = int(input(f"{Fore.BLUE}Enter Install (1), uninstall (0) apps mode or 99 to exit (1 / 0 / 99): {Fore.RESET}"))
            if mode == 99:
                break
            if mode != 1 and mode != 0 and mode != 99:
                print(f"{Style.BRIGHT}{Fore.RED}You must enter number.")
                break
            number = int(input(f"{Style.BRIGHT}{Fore.BLUE}Enter number: {Style.NORMAL}{Fore.RESET}"))
        except ValueError:
            print(f"{Style.BRIGHT}{Fore.RED}You must enter number.")
            pass
        except KeyboardInterrupt:
            print(f"{Style.BRIGHT}{Fore.RED}\nJust enter 99 to exit!")
            time.sleep(0.5)
            pass
        except:
            print(f"{Style.BRIGHT}{Fore.BLACK}Unknown Error!")
        else:
            if mode == 1:
                inMode = InstallMode(number)
                inMode.check_number()
            elif mode == 0:
                inMode = UninstallMode(number)
                inMode.check_number()
