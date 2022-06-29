import os
import wget
import colorama
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
        Install.wireshark()
        Install.nordvpn()
        Install.gparted()
        Install.gnometweaks()
        Install.zsh_p10k()
        Install.protonvpn()
        Install.nala()
    def librewolf(): #WARNING! It works with Ubuntu 2022.04 (jammy) based distros. Script from librewolf developer don't work properly (or it my mistake), so if you need to use other distro enter instead 'jammy' *other distro name*
        os.system('echo "deb [arch=amd64] http://deb.librewolf.net jammy main" | sudo tee /etc/apt/sources.list.d/librewolf.list')
        os.system('sudo wget https://deb.librewolf.net/keyring.gpg -O /etc/apt/trusted.gpg.d/librewolf.gpg')
        os.system('sudo apt update -y')
        os.system('sudo apt install librewolf -y')

    def telegram():
        wget.download('https://telegram.org/dl/desktop/linux', 'telegram.tar.xz')
        os.system('tar -xf telegram.tar.xz -C ~/')
        print("\nNow, u can leave app. It added to your app list.")
        os.system('~/Telegram/Telegram && rm telegram*') #Start Telegram (to add icon in app list) and removing Telegram installer (cleaning workdir)

    def veracrypt():
        #Getting VeraCrypt Developers public key and verifying it.
        wget.download('https://www.idrix.fr/VeraCrypt/VeraCrypt_PGP_public_key.asc', 'veracrypt_pub_key.asc')
        os.system('gpg --import veracrypt_pub_key.asc')
        url = 'https://launchpad.net/veracrypt/trunk/1.25.9/+download/veracrypt-1.25.9-Ubuntu-22.04-amd64.deb'
        wget.download(url, 'veracrypt.deb')
        url = 'https://launchpad.net/veracrypt/trunk/1.25.9/+download/veracrypt-1.25.9-Ubuntu-22.04-amd64.deb.sig'
        wget.download(url, 'veracrypt.deb.sig')
        os.system('gpg --verify veracrypt.deb.sig')
        input("Please, check that it Good Signature and press enter.")
        #Installing and cleaning workdir
        os.system('sudo apt install ./veracrypt.deb -y && rm veracrypt*')

    def virtualbox():
        os.system('sudo apt install virtualbox -y')

    def keepassxc():
        os.system('sudo add-apt-repository ppa:phoerious/keepassxc -y') #Adding official KeePassXC repo
        os.system('sudo apt update -y')
        os.system('sudo apt install keepassxc -y') #Installing latest version

    def discord():
        os.system('curl -L https://discord.com/api/download\?platform\=linux\&format\=deb > discord.deb')
        os.system('sudo apt install ./discord.deb -y')
        os.system('rm discord*')

    def qbittorrent():
        os.system('sudo apt install qbittorrent -y')

    def wireshark():
        os.system('sudo apt install wireshark -y')
        os.system('sudo dpkg-reconfigure wireshark-common -y')

    def nordvpn():
        os.system('curl https://repo.nordvpn.com/deb/nordvpn/debian/pool/main/nordvpn-release_1.0.0_all.deb > nordvpn.deb')
        #Installing nordvpn and cleaning workdir
        os.system('sudo apt install ./nordvpn.deb -y && sudo apt update -y && sudo apt install nordvpn -y && rm nordvpn*')
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
        print('You may install additional font for your ZSH theme.')
        os.system('sudo apt install zsh curl git -y')
        os.system('sudo chsh $USER -s /usr/bin/zsh')
        os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended')
        os.system('git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k')
        os.system('rm ~/.zshrc && cp .zshrc ~/.zshrc')
        print("{Style.BRIGHT}{Fore.RED}You need to relogin to your account or reboot computer to change your default shell to ZSH.")

    def protonvpn():
        wget.download('https://protonvpn.com/download/protonvpn-stable-release_1.0.1-1_all.deb', 'protonvpn.deb')
        os.system('sudo apt install ./protonvpn.deb -y && sudo apt update -y && sudo apt install protonvpn -y')
        os.system('sudo apt install gnome-shell-extension-appindicator gir1.2-appindicator3-0.1 -y')
        os.system('rm proton*')

    def nala():
        os.system('echo "deb http://deb.volian.org/volian/ scar main" | sudo tee /etc/apt/sources.list.d/volian-archive-scar-unstable.list && wget -qO - https://deb.volian.org/volian/scar.key | sudo tee /etc/apt/trusted.gpg.d/volian-archive-scar-unstable.gpg > /dev/null')
        os.system('sudo apt update -y && sudo apt install nala -y')
