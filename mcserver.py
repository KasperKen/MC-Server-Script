#
# title         Minecraft Server Automation Script
#
# description   Script to automate the installation of a minecraft server, and Java
#
# authors       Kenneth Andrews, Tanner Gibson, Fredrick Paulin
#
# licence       Gnu General Public License v2.0
#
# Copyright     2014 Kenneth Andrews, Tanner Gibson, Fredrick Paulin
#..........................................................................................
import sys
import urllib2

def downloader(url):
        u = urllib2.urlopen(url)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"[%3.2f%%]" % (file_size_dl * 100. / file_size)
            print status
            print ""

        f.close()
        

print "Minecraft Server install script"

install = raw_input ("would you like to install minecraft server? (y)es (n)o: ")
if install == ("n"):
        sys.exit()
print "Choose the server version you would like to download, and wait for the download to finish..."
print "1. Vanilla\n2. Bukkit"
print "Vanillia is the origional Server straight from minecraft.net,\nBukkit is oriented towards modders. If you are unsure choose vanilla."

server_type = raw_input ("Which version would you like to download? (1 or 2): ")

if server_type == ("1"): #Downloads Minecraft Server file based on users choice
        url = ("https://s3.amazonaws.com/Minecraft.Download/versions/1.7.4/minecraft_server.1.7.4.jar")
        
if server_type == ("2"):
        url = ("http://dl.bukkit.org/downloads/craftbukkit/get/01845_1.4.7-R1.0/craftbukkit.jar")

#This method of downloading the server works quite well. Implement it for other downloads.
file_name = "mcserver.jar"
downloader(url)

java = raw_input("Would you like the script to download java? (y/n): ")
if java == ("y"):
        if sys.platform == ("win32"): #If OS is detected as windows downloads java.exe
                java = raw_input ("Your system has Been detected as Windows. are you sure you want to downlad java?: ")
                if java == ("y"):
                        url=("http://download.oracle.com/otn-pub/java/jdk/7u45-b18/jre-7u45-windows-i586-iftw.exe")
                        downloader(url)
                        
                elif java == ("n"):
                        pass

        elif sys.platform == ("linux") or sys.platform == ("linux2"): #If OS is detected as Linux downloads java.tar.gz
                java = raw_input ("your System has been detected as Linux. It is reccomended that you install java manually through your distro's repository. would you like to continue?: ")
                if java == ("y"):
                        url = ("http://download.oracle.com/otn-pub/java/jdk/7u45-b18/jre-7u45-linux-i586.tar.gz")
                        downloader(url)

                
                elif java == ("n"):
                        pass

        else:
                print ("Sorry, the script was unable to detect your operating system. please install java manually.")

#       check for platform again, and decide how to install java based on sys.platform
#       if sys.platform == ("win32"):
#               install .\java.exe

#       elif sys.platform == ("linux") or sys.platform == ("linux2"):
#               extract, and install ./java.tar.gz

else:
        pass

admin = raw_input("Name of Admin?: ")

print "If you are unsure of whitelist choose 'false'"
whitelist = raw_input("enable whitelist?: (true) (false): ")

if whitelist == ("true"):
        whitelist_names = raw_input("User names of whitelisted players. serparate players with ',': ")

elif whitelist == ("false"):
        pass

print ("The rest of the settings are optional. if you choose no they will be set to defaults")
print "Now this one is a hard one if unknown google how to find it we are working on how to find server ip address"
ip= raw_input("server ip: ")

options = raw_input("would you like to change the default settings? (y)es (n)o: ")

if options == ("y"):
        monsters = raw_input("enable monsters?: ")
        animals = raw_input("spawn animals?: ")
        npc = raw_input("spawn NPCs?: ")
        structures = raw_input("generate structures?: ")
        pvp = raw_input("enable pvp?: ")
        print "Only disable this option if you will be playing without internet"
        online = raw_input("enable online mode?: ")
        print "if a character dies their banned from the server"
        hardcore = raw_input("enable hardcore mode?: ")
        print "if not sure set to 25565"
        port = raw_input("port number?: ")
        print "disable if not sure"
        rcon = raw_input("enable rcon?: ")
        print "used for generating maps, if unsure leave blank"
        seed = raw_input("map seed?: ")
        print "URL link for Texture pack download, if unsure leave blank"
        texture = raw_input("texture pack?: ")
        print "if unsure disable"       
        query = raw_input("enable query?: ")
        print "(1.survival) (2.creative)"
        gamemode = raw_input("gamemode?: ")
        print "(0.peacefull)(1.easy) (2.normal) (3.hard)"
        difficulty = raw_input("difficulty? 0-3: ")
        print "Message to apear on server list"
        motd = raw_input("MODT?: ")
        print "reccomended 256"
        build = raw_input("build height?: ")
        print "(1.default) (2.flatland) default reccomended"
        Map_type = raw_input("map type? 1-2: ")
        print "if not sure leave blank"
        generator_settings = raw_input("generator settings?: ")
        print "reccomended 10"
        view = raw_input("view distance?: ")
        nether = raw_input("allow nether (true), (false)?: ")
        flight= raw_input("allow flight?: ")
        print "Now this one is a hard one if unknown google how to find it we are working on how to find server ip address"
        ip= raw_input("server ip: ")
        debug= raw_input("debugging: ")
        snooper= raw_input("snooper setting: ")
        max_players= raw_input("max player: ")
else:
        ##Default Minecraft server properties via http://minecraft.gamepedia.com/Server.properties as of 1/12/14
##        generator_settings=
##        op-permission-level=4
##        level-name=world
##        enable-query=false
##        allow-flight=false
##        announce-player-achievements=true
##        server-port=25565
##        level-type=DEFAULT
##        enable-rcon=false
##        level-seed=
##        force-gamemode=false
##        server-ip=
##        max-build-height=256
##        spawn-npcs=true
##        white-list=false
##        spawn-animals=true
##        hardcore=false
##        snooper-enabled=true
##        online-mode=true
##        resource-pack=
##        pvp=true
##        difficulty=1
##        enable-command-block=false
##        gamemode=0
##        player-idle-timeout=0
##        max_players=20
##        spawn-monsters=true
##        generate-structures=true
##        view-distance=10
##        motd=A Minecraft Server
        ##Generates values for default set 
        monsters = "true"
        animals = "true"
        npc = "true"
        structures = "true"
        pvp = "true"
        online = "true"
        hardcore = "false"
        port = "25565"
        rcon = "false"
        seed = ""
        texture =""
        query = "false"
        gamemode = "0"
        difficulty = "1"
        motd = "Auto Generated Minecraft Server"
        build = "256"
        Map_type = "1"
        generator_settings = ""
        view = "10"
        nether = "true"
        flight= "false"
        debug= ""
        snooper= "true"
        max_players= "20"      


#if user decided to change default values then write them to server.properties if not ignore.
#if options == ("y"):
        #write all changes to file
server_props = ("""generator_settings=%s
allow-nether=%s
level-name=world
enable-query=%s
allow-flight=%s
server-port=%s
query.port=%s
evel-type=%s
enable-rcon=%s
level-seed=%s
server-ip=%s
max-build-height=%s
spawn-ncps=%s
white-list=%s
debug=%s
spawn-animals=%s
texture-pack=%s
snooper-enabled=%s
hardcore=%s
online-mode=%s
pvp=%s
difficulty=%s
gamemode=%s
max-players=%s
spawn-monsters=%s
generate-structures=%s
view-distance=%s
spawn-protection=false
motd=%s
"""%(generator_settings, nether, query, flight, port, port, Map_type, rcon, seed, ip, build,
npc, whitelist, debug, animals, texture, snooper, hardcore, online, pvp, difficulty,
gamemode, max_players, monsters, structures, view, motd))

filename = ("server.properties")
target = open(filename, 'w')
target.write(server_props)
target.close

#create batch/bash script in server directory to start server
batch = "java -Xms512M -Xmx1G -jar mcserver.jar"
filename = ("start-server.bat")
target = open(filename, 'w')
target.write(batch)
target.close

print "The program has finished setting up your server!"



#create desktop shortcut with icon to startup script

#get python to run the batch file
#               The following is me testing to see if I can get python to start the server.
##start_server = raw_input("Would you like to start your server now? (y)es (n)o: ")
##if start_server == ("y"):
##        import subprocess
##
##        p = subprocess.Popen('start-server.bat', creationflags=subprocess.CREATE_NEW_CONSOLE)
