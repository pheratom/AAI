from appInstaller import Install
from appUninstaller import unInstall
import sys
class InstallMode:
    def __init__(self, number):
        self.number = number
        pass
    def check_number(self):
        if self.number == 99:
            sys.exit()
        elif self.number == 0:
            Install.all()
        elif self.number == 1:
            Install.librewolf()
        elif self.number == 2:
            Install.telegram()
        elif self.number == 3:
            Install.veracrypt()
        elif self.number == 4:
            Install.virtualbox()
        elif self.number == 5:
            Install.keepassxc()
        elif self.number == 6:
            Install.discord()
        elif self.number == 7:
            Install.qbittorrent()
        elif self.number == 8:
            Install.nordvpn()
        elif self.number == 9:
            Install.gparted()
        elif self.number == 10:
            Install.gnometweaks()
        elif self.number == 11:
            Install.zsh_p10k()
        elif self.number == 12:
            Install.protonvpn()
        elif self.number == 13:
            Install.nala()
        else:
            print(f"{Style.BRIGHT}{Fore.RED}You entered wrong number!")

class UninstallMode:
    def __init__(self, number):
        self.number = number
        pass
    def check_number(self):
        if self.number == 99:
            sys.exit()
        elif self.number == 0:
            unInstall.all()
        elif self.number == 1:
            unInstall.librewolf()
        elif self.number == 2:
            unInstall.telegram()
        elif self.number == 3:
            unInstall.veracrypt()
        elif self.number == 4:
            unInstall.virtualbox()
        elif self.number == 5:
            unInstall.keepassxc()
        elif self.number == 6:
            unInstall.discord()
        elif self.number == 7:
            unInstall.qbittorrent()
        elif self.number == 8:
            unInstall.nordvpn()
        elif self.number == 9:
            unInstall.gparted()
        elif self.number == 10:
            unInstall.gnometweaks()
        elif self.number == 11:
            unInstall.zsh_p10k()
        elif self.number == 12:
            unInstall.protonvpn()
        elif self.number == 13:
            unInstall.nala()
        else:
            print(f"{Style.BRIGHT}{Fore.RED}You entered wrong number!")
