import os


def update():
    os.system("sudo apt update -y")


def sublime_text():
    os.system(
        """wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -""")
    os.system("""sudo apt-get install apt-transport-https""")
    os.system("""echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list""")


def snapd():
    os.system("sudo apt install snapd")


def snap_store():
    os.system("sudo snap install snap-store")


def vlc():
    """
    VLC for Ubuntu and many other Linux distributions is packaged using snapcraft. This allows us to distribute latest and greatest VLC versions directly to end users, with security and critical bug fixes, full codec and optical media support.
    If you wish to install the traditional deb package, it is available as usual via APT, with all security and critical bug fixes. However, there will be no major VLC version updates until the next Ubuntu release.

    Read more on:
        https://www.videolan.org/vlc/download-ubuntu.html
    """
    os.system("sudo snap install vlc")


def vscode(itype: str = "apt"):
    if itype.lower() == "apt":
        os.system(
            "wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg")
        os.system(
            "sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/")
        os.system(
            """sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'""")
        os.system("rm -f packages.microsoft.gpg")
        os.system("sudo apt install apt-transport-https")
        update()
        os.system("sudo apt install code")

    elif itype.lower() == "snap":
        os.system("sudo snap install --classic code")


def pip3():
    os.system("sudo apt install python3-pip")


def pip():
    os.system("sudo apt install python-pip")


def java_development_kit():
    os.system("sudo apt install default-jdk")


def spotify(itype: str = "apt"):
    if itype == "snap":
        os.system("sudo snap install spotify")
    elif itype == "apt":
        os.system(
            "curl -sS https://download.spotify.com/debian/pubkey_0D811D58.gpg | sudo apt-key add - ")
        os.system(
            """echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list""")
        os.system("sudo apt-get update && sudo apt-get install spotify-client")


def eclipse():
    os.system("sudo snap install eclipse --classic")


def pycharm(dtype: str = "community"):
    if dtype == "community":
        os.system("sudo snap install pycharm-professional --classic")
    elif dtype == "professional":
        os.system("sudo snap install pycharm-community --classic")
    elif dtype == "educational":
        os.system("sudo snap install pycharm-educational --classic")


def htop(itype: str = "apt"):
    if itype == "apt":
        os.system("sudo apt install htop")
    else:
        os.system("sudo snap install htop")


def shotcut(itype: str = "apt"):
    if itype == "apt":
        os.system("sudo add-apt-repository ppa:haraldhv/shotcut")
        os.system("sudo apt-get update && sudo apt-get upgrade")
        os.system("sudo apt install shotcut")
    else:
        os.system("sudo snap install shotcut --classic")


def ffmpeg(itype: str = "apt"):
    if itype == "apt":
        os.system("sudo apt install ffmpeg")
    else:
        os.system("sudo snap install ffmpeg")


def bitwarden():
    os.system("sudo snap install bitwarden")


def nmap(itype: str = "apt"):
    if itype == "apt":
        os.system("sudo apt-get install nmap")
    else:
        os.system("sudo snap install nmap")


def clementine(itype: str = "apt"):
    if itype == "apt":
        os.system("sudo apt install clementine")
    else:
        os.system("sudo snap install clementine")


def only_office():
    os.system("sudo snap install onlyoffice-desktopeditors")


def youtube_dl(itype: str = "snap"):
    if itype == "snap":
        os.system("sudo snap install youtube-dl")
    else:
        os.system("pip3 install youtube-dl")


def blender():
    os.system("sudo snap install blender --classic")


def wget():
    os.system("apt-get install wget")


def google_chrome():
    os.system(
        "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("sudo dpkg -i google-chrome-stable_current_amd64.deb")


def minecraft(itype: str = "snap"):
    if itype == "snap":
        os.system("sudo snap install mc-installer")
        os.system("sudo snap run mc-installer")  # im not sure about this
    else:
        os.system("wget https://launcher.mojang.com/download/Minecraft.deb")
        os.system("sudo dpkg -i Minecraft.deb")
        os.system("sudo apt -f install")
