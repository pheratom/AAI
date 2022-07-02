import os
import wget
import colorama
import time
import sys
import subprocess
import requests
from colorama import Fore, Back, Style
class Install:
    def __init__(self):
        pass
    def all():
        Install.librewolf()
        Install.telegram()
        Install.veracrypt()
        Install.virtualbox()
        Install.keepassxc()
        Install.discord()
        Install.qbittorrent()
        Install.nordvpn()
        Install.gparted()
        Install.gnometweaks()
        Install.protonvpn()
        Install.nala()
        Install.zsh_p10k()
    def librewolf(): #It saves {name of linux distro} in temporary file. Then it copies {name of linux distro} in string and add LibreWolf source repo. (because scipts from developers don't work ¯\_(ツ)_/¯).
        command = "lsb_release -sc > temp.txt"
        os.system(command)
        with open('temp.txt', 'r') as file:
            distro = file.read()
            distro = distro.strip('\n')
        if distro != 'bullseye' and distro != 'focal' and distro != 'impish' and distro != 'jammy' and distro != 'uma' and distro != 'una':
            distro = 'focal'
        os.system(f'echo "deb [arch=amd64] http://deb.librewolf.net {distro} main" | sudo tee /etc/apt/sources.list.d/librewolf.list')
        os.system('sudo wget https://deb.librewolf.net/keyring.gpg -O /etc/apt/trusted.gpg.d/librewolf.gpg')
        os.system('sudo apt update -y')
        os.system('sudo apt install librewolf -y')
        os.system('rm temp.txt')

    def telegram():
        wget.download('https://telegram.org/dl/desktop/linux', 'telegram.tar.xz')
        os.system('tar -xf telegram.tar.xz -C ~/')
        os.system('~/Telegram/Telegram &')
        os.system('rm telegram*')
        print(f"{Fore.RED}Telegram will close automatically!")
        time.sleep(5)
        os.system('sudo pkill Telegram') #Auto add telegram icon in app list

    def veracrypt():
        #Getting VeraCrypt Developers public key and verifying it.
        response = requests.get("https://api.github.com/repos/veracrypt/VeraCrypt/releases/latest")
        full_version_name = response.json()["name"]
        full_version_name = full_version_name.split()
        version = full_version_name[-1]
        wget.download(f'https://launchpad.net/veracrypt/trunk/{version}/+download/veracrypt-{version}-Ubuntu-22.04-amd64.deb', 'veracrypt.deb')
        wget.download(f'https://launchpad.net/veracrypt/trunk/{version}/+download/veracrypt-{version}-Ubuntu-22.04-amd64.deb.sig', 'veracrypt.deb.sig')
        wget.download('https://www.idrix.fr/VeraCrypt/VeraCrypt_PGP_public_key.asc', 'veracryptpublickey.asc')
        os.system('gpg --import veracryptpublickey.asc')
        command = "gpg --verify veracrypt.deb.sig 2>temp.txt"
        os.system(command)
        with open('temp.txt', 'r') as file:
            result = file.read()
        if 'Good signature' in result:
            print(f"{Fore.GREEN}{Style.BRIGHT}Signature verify success!")
            os.system('sudo apt install ./veracrypt.deb -y')
            os.system('rm veracrypt*')
            os.system('rm temp.txt')
        elif 'Bad signature' in result:
            print(f"{Fore.RED}{Style.BRIGHT}Signature verify failed! Somebody can do something bad! Exitting.")
            sys.exit()

    def virtualbox():
        os.system('sudo apt install virtualbox -y')

    def keepassxc():
        os.system('sudo add-apt-repository ppa:phoerious/keepassxc -y') #Adding official KeePassXC repo
        os.system('sudo apt update -y')
        os.system('sudo apt install keepassxc -y') #Installing latest version

    def discord():
        os.system('sudo apt install curl -y')
        os.system('curl -L https://discord.com/api/download\?platform\=linux\&format\=deb > discord.deb')
        os.system('sudo apt install ./discord.deb -y')
        os.system('rm discord*')

    def qbittorrent():
        os.system('sudo apt install qbittorrent -y')

    def nordvpn():
        os.system('sudo apt install curl -y')
        os.system('curl https://repo.nordvpn.com/deb/nordvpn/debian/pool/main/nordvpn-release_1.0.0_all.deb > nordvpn.deb')
        #Installing nordvpn and cleaning workdir
        os.system('sudo apt install ./nordvpn.deb -y && sudo apt update -y && sudo apt install nordvpn -y && rm nordvpn.deb')
        print("Recommended to log out user account. (to avoid NordVPN bug.)")

    def gparted():
        os.system('sudo apt install gparted -y')

    def gnometweaks():
        os.system('sudo apt install gnome-tweaks -y')

    def zsh_p10k():
        print(f"""{Fore.RED}{Style.BRIGHT}
                                .__            ____  ._. 
__  _  _______  _______   ____  |__|  ____    / ___\ | | 
\ \/ \/ /\__  \ \_  __ \ /    \ |  | /    \  / /_/  >| | 
 \     /  / __ \_|  | \/|   |  \|  ||   |  \ \___  /  \| 
  \/\_/  (____  /|__|   |___|  /|__||___|  //_____/   __ 
              \/             \/          \/           \/ """)
        print(f'{Back.RED}You may install additional font for your ZSH theme.')
        print(f'{Back.RED}https://github.com/romkatv/powerlevel10k/blob/master/font.md')
        os.system('sudo apt install zsh curl git -y')
        os.system('rm -rf ~/.oh-my-zsh')
        os.system('sudo chsh $USER -s /usr/bin/zsh')
        os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended')
        os.system('git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k')
        os.system('rm ~/.zsh*')
        zsh_content = """
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="powerlevel10k/powerlevel10k"
plugins=(git)
source $ZSH/oh-my-zsh.sh"""
        with open('.zshrc', 'w') as file:
            file.write(zsh_content)
        os.system('cp .zshrc ~/.zshrc && rm .zshrc')
        print(f"{Fore.RED}Sometimes default shell don't change. To avoid it just relogin your account or reboot computer.")

    def protonvpn():
        wget.download('https://protonvpn.com/download/protonvpn-stable-release_1.0.1-1_all.deb', 'protonvpn.deb')
        os.system('sudo apt install ./protonvpn.deb -y && sudo apt update -y && sudo apt install protonvpn -y')
        os.system('sudo apt install gnome-shell-extension-appindicator gir1.2-appindicator3-0.1 -y')
        os.system('rm proton*')

    def nala():
        os.system('echo "deb http://deb.volian.org/volian/ scar main" | sudo tee /etc/apt/sources.list.d/volian-archive-scar-unstable.list && wget -qO - https://deb.volian.org/volian/scar.key | sudo tee /etc/apt/trusted.gpg.d/volian-archive-scar-unstable.gpg > /dev/null')
        os.system('sudo apt update -y && sudo apt install nala -y')
