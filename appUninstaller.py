import os
import wget
import colorama
from colorama import Fore, Back, Style
class unInstall:
    def __init__(self):
        pass

    def all():
        unInstall.librewolf()
        unInstall.telegram()
        unInstall.veracrypt()
        unInstall.virtualbox()
        unInstall.keepassxc()
        unInstall.discord()
        unInstall.qbittorrent()
        unInstall.nordvpn()
        unInstall.gparted()
        unInstall.gnometweaks()
        unInstall.zsh_p10k()
        unInstall.protonvpn()
        unInstall.nala()

    def librewolf():
        os.system('sudo rm /etc/apt/sources.list.d/librewolf.list && sudo rm /etc/apt/trusted.gpg.d/librewolf.gpg')
        os.system('sudo apt purge librewolf -y && rm -rf ~/.librewolf && sudo apt update')
        os.system('sudo apt autoremove -y')

    def telegram():
        os.system('rm -rf ~/Telegram && rm -rf ~/.local/share/TelegramDesktop')
        os.system('rm -rf ~/.local/share/applications/*Telegram_Desktop.desktop')
        os.system('rm -rf ~/.local/share/applications/userapp-Telegram*')

    def veracrypt():
        os.system('sudo apt purge veracrypt -y')
        os.system('{Style.BRIGHT}{Fore.RED}Warning, it don\'t delete VeraCrypt Developers public key!')
        os.system('sudo apt autoremove -y')

    def virtualbox():
        os.system('sudo apt purge virtualbox -y')
        os.system('sudo apt autoremove -y')

    def keepassxc():
        os.system('sudo apt purge keepassxc -y && sudo rm /etc/apt/trusted.gpg.d/phoerious-ubuntu-keepassxc* && sudo rm /etc/apt/sources.list.d/phoerious-ubuntu-keepassxc*')
        os.system('sudo apt update -y')
        os.system('sudo apt autoremove -y')

    def discord():
        os.system('sudo apt purge discord -y && rm -rf ~/.config/discord')
        os.system('sudo apt autoremove -y')

    def qbittorrent():
        os.system('sudo apt purge qbittorrent -y')
        os.system('sudo apt autoremove -y')

    def nordvpn():
        os.system('sudo apt purge nordvpn nordvpn-release -y && sudo rm /etc/apt/sources.list.d/nordvpn* && sudo rm /etc/apt/trusted.gpg.d/nordvpn*')
        os.system('sudo apt update -y')
        os.system('sudo apt autoremove -y')

    def gparted():
        os.system('sudo apt purge gparted -y')
        os.system('sudo apt autoremove -y')

    def gnometweaks():
        os.system('sudo apt purge gnome-tweaks -y')
        os.system('sudo apt autoremove -y')

    def zsh_p10k():
        os.system('sudo chsh $USER -s /bin/bash')
        os.system('sudo apt purge zsh -y && rm -rf ~/.zsh* && rm ~/.oh-my-zsh && rm -rf ~/.p10k* && rm -rf ~/..shell.pre-oh-my-zsh')
        os.system('sudo apt autoremove -y')

    def protonvpn():
        os.system('sudo apt purge protonvpn -y && rm -rf ~/.cache/protonvpn && rm -rf ~/.config/protonvpn')
        os.system('sudo apt autoremove -y')

    def nala():
        os.system('sudo apt purge nala -y && sudo rm /etc/apt/sources.list.d/volian-archive* && sudo rm /etc/apt/trusted.gpg.d/volian-archive*')
        os.system('sudo apt autoremove -y')
