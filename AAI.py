import os
import time
import colorama
import sys
from colorama import Fore, Back, Style
try:
    from appInstaller import Install
except ModuleNotFoundError:
    print(f"{Fore.RED}You did't installed requirement packages.")
    answer = input(f"Install packages? (y/n) ")
    if answer == 'y':
        os.system('python3 -m pip install wget && python3 -m pip install colorama')
        pass
    elif answer == 'n':
        print(f"Ok, exitting...")
        sys.exit()
    else:
        print("You need to type 'y' or 'n'. Nothing else!")
        sys.exit()
else:
    from appInstaller import Install
colorama.init(autoreset = True)
def printAppList():
    print(f""" {Fore.CYAN}
Select app: {Fore.BLUE}
\t0 - Install App Listed Apps
\t1 - Librewolf
\t2 - Telegram
\t3 - Veracrypt
\t4 - Virtualbox
\t5 - KeePassXC
\t6 - Discord
\t7 - QBitTorrent
\t8 - Wireshark
\t9 - NordVPN
\t10 - GParted
\t11 - Gnome Tweaks
\t12 - ZSH + PowerLevel10k
\t13 - ProtonVPN
\t14 - Nala (APT FrontEnd)
\t99 - Exit
""")

if __name__ == '__main__':
    print(Fore.GREEN + '''
                     _____        __  __ 
     /\        /\   |_   _|      /_ |/_ |
    /  \      /  \    | |   __   _| | | |
   / /\ \    / /\ \   | |   \ \ / / | | |
  / ____ \  / ____ \ _| |_   \ V /| |_| |
 /_/    \_\/_/    \_\_____|   \_(_)_(_)_|''') #https://www.fontchanger.net/ascii-text.html Font - Big
    while True:
        printAppList()
        try:
            number = int(input(f"{Style.BRIGHT}Enter number: {Style.NORMAL}"))
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
            if number == 99:
                break
            elif number == 0:
                Install.all()
            elif number == 1:
                Install.librewolf()
            elif number == 2:
                Install.telegram()
            elif number == 3:
                Install.veracrypt()
            elif number == 4:
                Install.virtualbox()
            elif number == 5:
                Install.keepassxc()
            elif number == 6:
                Install.discord()
            elif number == 7:
                Install.qbittorrent()
            elif number == 8:
                Install.wireshark()
            elif number == 9:
                Install.nordvpn()
            elif number == 10:
                Install.gparted()
            elif number == 11:
                Install.gnometweaks()
            elif number == 12:
                Install.zsh_p10k()
            elif number == 13:
                Install.protonvpn()
            elif number == 14:
                Install.nala()
            else:
                print(f"{Style.BRIGHT}{Fore.RED}You entered wrong number!")
