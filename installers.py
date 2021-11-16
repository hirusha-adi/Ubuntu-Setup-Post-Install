import os


def update_system():
    os.system("sudo apt update")
    os.system("sudo apt upgrade -y")


def sublime_text(mode: str = "snap"):
    if mode == "apt":
        os.system(
            """wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -""")
        os.system("""sudo apt-get install apt-transport-https""")
        os.system(
            """echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list""")
        os.system("sudo apt update -y")
        os.system("sudo apt install sublime-text -y")
    else:
        os.system("sudo snap install sublime-text --classic")


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
        os.system("sudo apt update")
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
        os.system("sudo apt -f install -y")  # im not sure if it should be here


def teams():
    os.system("sudo snap install teams")


def zoom():
    os.system("sudo snap install zoom-client")


def notion():
    os.system("sudo snap install notion-snap")


def skype():
    os.system("sudo snap install skype")


def konversation():
    os.system("sudo snap install konversation")


def slack():
    os.system("sudo snap install slack --classic")


def brave():
    os.system("sudo snap install brave")


def handbrake_jz():
    os.system("sudo snap install handbrake-jz")


def instagraph():
    os.system("sudo snap install instagraph")


def docker():
    os.system("sudo snap install docker")


def tor_middle_relay():
    os.system("sudo snap install tor-middle-relay")


def audacity():
    os.system("sudo snap install audacity")


def google_play_music_desktop_player():
    os.system("sudo snap install google-play-music-desktop-player")


def qbittorrent():
    os.system("sudo snap install qbittorrent-arnatious")


def github_desktop():
    os.system("sudo wget https://github.com/shiftkey/desktop/releases/download/release-2.9.3-linux3/GitHubDesktop-linux-2.9.3-linux3.deb")
    os.system("sudo gdebi GitHubDesktop-linux-2.9.3-linux3.deb")


def obs_studio():
    os.system("sudo snap install obs-studio")


def virtualbox(mode: str = "old"):
    if mode == "old":
        os.system("sudo apt install virtualbox")
    else:
        os.system(
            "wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -")
        os.system(
            'sudo add-apt-repository "deb [arch=amd64] http://download.virtualbox.org/virtualbox/debian $(lsb_release -cs) contrib"')
        os.system("sudo apt update && sudo apt install virtualbox")


def whatsapp():
    os.system("sudo snap install whatsapp-for-linux")


def discord():
    os.system("sudo snap install discord")


def flameshot():
    os.system("sudo snap install flameshot")


def spectacle():
    os.system("sudo snap install spectacle")


def anydesk():
    os.system(
        "wget -qO - https://keys.anydesk.com/repos/DEB-GPG-KEY | sudo apt-key add -")
    os.system(
        'echo "deb http://deb.anydesk.com/ all main" | sudo tee /etc/apt/sources.list.d/anydesk-stable.list')
    os.system("sudo apt update")
    os.system("sudo apt install anydesk")


def teamviewer():
    os.system(
        'wget https://download.teamviewer.com/download/linux/teamviewer_amd64.deb')
    os.system('sudo dpkg -i ./teamviewer_amd64.deb')


def steam():
    os.system("sudo apt install steam-installer")


def telegram():
    os.system("sudo snap install telegram-desktop")


def tor_browser():
    os.system("sudo add-apt-repository ppa:micahflee/ppa")
    os.system("sudo apt update")
    os.system("sudo apt install torbrowser-launcher")


def yakyak():
    os.system("sudo snap install yakyak")


def signal():
    os.system("sudo snap install signal-desktop")


def chromium():
    os.system("sudo snap install chromium")


def figlet():
    os.system("sudo apt-get install -y figlet")


def RUN_PROGRAM():
    def show_logo():
        print("""
     ____       _     _             
    |  _ \  ___| |__ (_) __ _ _ __  
    | | | |/ _ \ '_ \| |/ _` | '_ \ 
    | |_| |  __/ |_) | | (_| | | | |
    |____/ \___|_.__/|_|\__,_|_| |_|
             Installer v1.0
        """)
    os.system("clear")
    show_logo()

    update_system()
    snapd()

    instpe = input(
        "? What do you want to be the default to be? Apt or Snap: ")
    if instpe.lower().startswith("s"):
        dlpkgmgr = "snap"
    else:
        dlpkgmgr = "apt"

    print("+ You will be given the package name and a what that package is about.\n+ Enter 'y' to install and any other letter to skip it and continue.")

    msublime_text = input("? Sublime Text (Text Editor): ")
    if msublime_text.lower().startswith("y"):
        sublime_text(mode=dlpkgmgr)
    else:
        print("- Skipping: Sublime Text")

    msnap_store = input("? Snap Store (Software Center): ")
    if msnap_store.lower().startswith("y"):
        snap_store(mode=dlpkgmgr)
    else:
        print("- Skipping: Snap Store")

    mvlc = input("? VLC (Media Player): ")
    if mvlc.lower().startswith("y"):
        vlc()
    else:
        print("- Skipping: VLC")

    mvscode = input("? Visual Studio Code (Development): ")
    if mvscode.lower().startswith("y"):
        vscode(itype=dlpkgmgr)
    else:
        print("- Skipping: Visual Studio Code")

    mpip3 = input("? Python3 Pip (Development): ")
    if mpip3.lower().startswith("y"):
        pip3()
    else:
        print("- Skipping: Python3 Pip")

    mpip2 = input("? Python2 Pip (Development): ")
    if mpip2.lower().startswith("y"):
        pip3()
    else:
        print("- Skipping: Python2 Pip")

    mjava_development_kit = input("? Java Development Kit (Development): ")
    if mjava_development_kit.lower().startswith("y"):
        pip()
    else:
        print("- Skipping: Java Development Kit")

    mspotify = input("? Spotify (Media Player): ")
    if mspotify.lower().startswith("y"):
        spotify(itype=dlpkgmgr)
    else:
        print("- Skipping: Spotify")

    meclipse = input("? Eclipse (Development): ")
    if meclipse.lower().startswith("y"):
        eclipse()
    else:
        print("- Skipping: Eclipse")

    mpycharmc = input("? PyCharm Community Edition (Development): ")
    if mpycharmc.lower().startswith("y"):
        pycharm(dtype="community")
    else:
        print("- Skipping: PyCharm Community Edition")

    mpycharmp = input("? PyCharm Professional Edition (Development): ")
    if mpycharmp.lower().startswith("y"):
        pycharm(dtype="professional")
    else:
        print("- Skipping: PyCharm Professional Edition")

    mpycharme = input("? PyCharm Educational Edition (Development): ")
    if mpycharme.lower().startswith("y"):
        pycharm(dtype="educational")
    else:
        print("- Skipping: PyCharm Educational Edition")

    mhtop = input("? Htop (System Monitor): ")
    if mhtop.lower().startswith("y"):
        htop(itype=dlpkgmgr)
    else:
        print("- Skipping: Htop")

    mshotcut = input("? Shot Cut (Video Editor): ")
    if mshotcut.lower().startswith("y"):
        shotcut(itype=dlpkgmgr)
    else:
        print("- Skipping: Shot Cut")

    mffmpeg = input("? FFMPEG (Media Tool): ")
    if mffmpeg.lower().startswith("y"):
        ffmpeg(itype=dlpkgmgr)
    else:
        print("- Skipping: FFMPEG")

    mbitwarden = input("? BitWarden (Password Manager): ")
    if mbitwarden.lower().startswith("y"):
        bitwarden()
    else:
        print("- Skipping: BitWarden")

    mnmap = input("? NMap (Network Scanner): ")
    if mnmap.lower().startswith("y"):
        nmap(itype=dlpkgmgr)
    else:
        print("- Skipping: NMap")

    mclementine = input("? Clementine (Media Player): ")
    if mclementine.lower().startswith("y"):
        clementine(itype=dlpkgmgr)
    else:
        print("- Skipping: Clementine")

    monly_office = input("? Only Office (Office Suite): ")
    if monly_office.lower().startswith("y"):
        only_office()
    else:
        print("- Skipping: Only Office")

    myoutube_dl = input("? YouTube-dl (Media Downloader): ")
    if myoutube_dl.lower().startswith("y"):
        youtube_dl(itype="snap")
    else:
        print("- Skipping: Only Office")

    mywget = input("? Wget (CLI-Utitlity): ")
    if mywget.lower().startswith("y"):
        wget()
    else:
        print("- Skipping: Wget")

    mblender = input("? Blender (Multimedia Creating Suite): ")
    if mblender.lower().startswith("y"):
        blender()
    else:
        print("- Skipping: Blender")

    mgoogle_chrome = input("? Minecraft Launcher (Game Launcher): ")
    if mgoogle_chrome.lower().startswith("y"):
        minecraft(itype=dlpkgmgr)
    else:
        print("- Skipping: Minecraft Launcher")

    mminecraft = input("? Google Chrome (Web Browser): ")
    if mminecraft.lower().startswith("y"):
        google_chrome()
    else:
        print("- Skipping: Google Chrome")

    mteams = input("? Microsoft Teams (Communication Platform): ")
    if mteams.lower().startswith("y"):
        teams()
    else:
        print("- Skipping: Microsoft Teams")

    mzoom = input("? Zoom (Communication Platform): ")
    if mzoom.lower().startswith("y"):
        zoom()
    else:
        print("- Skipping: Zoom")

    mnotion = input("? Notion (Notetaking Software): ")
    if mnotion.lower().startswith("y"):
        notion()
    else:
        print("- Skipping: Notion")

    mskype = input("? Skype (Communication Platform): ")
    if mskype.lower().startswith("y"):
        skype()
    else:
        print("- Skipping: Skype")

    mslack = input("? Slack (Communication Platform): ")
    if mslack.lower().startswith("y"):
        slack()
    else:
        print("- Skipping: Slack")

    mskonversation = input("? Konversation (IRC Client): ")
    if mskonversation.lower().startswith("y"):
        konversation()
    else:
        print("- Skipping: Konversation")

    mbrave = input("? Brave (Web Browser): ")
    if mbrave.lower().startswith("y"):
        brave()
    else:
        print("- Skipping: Brave")

    mhandbrake_jz = input("? Handbrake (Media Converter): ")
    if mhandbrake_jz.lower().startswith("y"):
        handbrake_jz()
    else:
        print("- Skipping: Handbrake")

    minstagraph = input("? Instagraph (Desktop Instagram Client): ")
    if minstagraph.lower().startswith("y"):
        instagraph()
    else:
        print("- Skipping: Instagraph")

    mdocker = input("? Docker (Development): ")
    if mdocker.lower().startswith("y"):
        docker()
    else:
        print("- Skipping: Docker")

    mtor_middle_relay = input("? Tor Middle Relay (Tor): ")
    if mtor_middle_relay.lower().startswith("y"):
        konversation()
    else:
        print("- Skipping: Tor Middle Relay")

    maudacity = input("? Audacity (Audio Editor): ")
    if maudacity.lower().startswith("y"):
        audacity()
    else:
        print("- Skipping: Audacity")

    mgoogle_play_music_desktop_player = input(
        "? Google Play Music Desktop Player (Media Players): ")
    if mgoogle_play_music_desktop_player.lower().startswith("y"):
        konversation()
    else:
        print("- Skipping: Google Play Music Desktop Player")

    mqbittorrent = input("? Qbittorrent (Torrent Client): ")
    if mqbittorrent.lower().startswith("y"):
        qbittorrent()
    else:
        print("- Skipping: Qbittorrent")

    mgithub_desktop = input("? GitHub Deskop (Development): ")
    if mgithub_desktop.lower().startswith("y"):
        github_desktop()
    else:
        print("- Skipping: GitHub Deskop")

    mobs_studio = input("? OBS Studio (Screencasting & Streaming app): ")
    if mobs_studio.lower().startswith("y"):
        obs_studio()
    else:
        print("- Skipping: OBS Studio")

    mvirtualbox = input("? VirtualBox (Hypervisor): ")
    if mvirtualbox.lower().startswith("y"):
        mvirtualbox1 = input(
            "? VirtualBox (Hypervisor) - Use Apt or get the Latest version: ")
        if mvirtualbox1.lower().startswith("a"):
            virtualbox(mode="old")
        else:
            virtualbox(mode="latest")
    else:
        print("- Skipping: VirtualBox")

    mwhatsapp = input("? WhatsApp (Messaging and VOIP): ")
    if mwhatsapp.lower().startswith("y"):
        audacity()
    else:
        print("- Skipping: WhatsApp")

    mdiscord = input("? Discord (Messaging and VOIP): ")
    if mdiscord.lower().startswith("y"):
        discord()
    else:
        print("- Skipping: Discord")

    mflameshot = input("? Flameshot (Screenshot Tool): ")
    if mflameshot.lower().startswith("y"):
        flameshot()
    else:
        print("- Skipping: Flameshot")

    mspectacle = input("? Spectacle (Screenshot Tool): ")
    if mspectacle.lower().startswith("y"):
        spectacle()
    else:
        print("- Skipping: Spectacle")

    manydesk = input("? Anydesk (Remote Desktop Application): ")
    if manydesk.lower().startswith("y"):
        anydesk()
    else:
        print("- Skipping: Anydesk")

    mteamviewer = input("? Teamviewer (Remote Desktop Application): ")
    if mteamviewer.lower().startswith("y"):
        teamviewer()
    else:
        print("- Skipping: Teamviewer")

    msteam = input("? Steam (Game Launcher): ")
    if msteam.lower().startswith("y"):
        teams()
    else:
        print("- Skipping: Steam")

    mtelegram = input("? Telegram (Messaging and VOIP): ")
    if mtelegram.lower().startswith("y"):
        telegram()
    else:
        print("- Skipping: Telegram")

    mtor_browser = input("? Tor Broswer (Web Browser): ")
    if mtor_browser.lower().startswith("y"):
        tor_browser()
    else:
        print("- Skipping: Tor Broswer")

    myakyak = input("? YakYak (Google Hangouts Desktop Client): ")
    if myakyak.lower().startswith("y"):
        yakyak()
    else:
        print("- Skipping: YakYak")

    msignal = input("? Signal (Messaging and VOIP): ")
    if msignal.lower().startswith("y"):
        signal()
    else:
        print("- Skipping: Signal")

    mfiglet = input("? Figlet (CLI-Utitlity): ")
    if mfiglet.lower().startswith("y"):
        figlet()
    else:
        print("- Skipping: Figlet")


if __name__ == "__main__":
    RUN_PROGRAM()
