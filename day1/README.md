### Benutze Putty von der Command Line
```bash
P:\portable\putty\putty.exe -ssh pi@raspberrypi3
```

### Preserve bash history in multiple terminal windows

Add the following to ~/.bashrc
```bash
#
#https://unix.stackexchange.com/questions/1288/preserve-bash-history-in-multiple-terminal-windows

# Avoid duplicates
export HISTCONTROL=ignoredups:erasedups  
# When the shell exits, append to the history file instead of overwriting it
shopt -s histappend

# After each command, append to the history file and reread it
export PROMPT_COMMAND="${PROMPT_COMMAND:+$PROMPT_COMMAND$'\n'}history -a; history -c; history -r"
```

### Andere praktische Skripte im Umgang mit der bash
```bash
# The script command is a Unix utility that records a terminal session. The scriptreplay command offers a replay function to script. The session is captured in file name typescript by default.
script

# If your local computer crashes or you lose the connection, the processes or login sessions you establish through screen don't go away.
screen
```

### Mount des Projektordners "raspiday" auf dem Memory Sticks an der Fritz.Box
```bash
sudo mkdir /raspiday
sudo mount -t cifs -o rw,file_mode=0777,dir_mode=0777,username=raspiday,password=raspiday //fritz.box/FRITZ.NAS/SanDisk-Ultra-01/raspiday /raspiday
ls -l /raspiday
```
(Schön dabei: Das raspbian kenn die cifs Treiber ohne zusätzlich Installation.)

### VNC-Server für Raspi: Konfiguration und Ändern der Auflösung:
Aus https://www.elektronik-kompendium.de/sites/raspberry-pi/2011121.htm

Konfiguration mit voller Auflösung:

-scale ist die "Lösung" <breite in pix.>x<hoehe in pix.>

```bash
[Unit]
Description=Start X11VNC
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/x11vnc -display :0 -scale 1920x1080 -auth guess -forever -lo$

[Install]
WantedBy=multi-user.target
```

### Den "raspberrypi3" (mosquitto broker) umstellen auf feste IP Adresse
Wir fanden folgende Lösung. 
https://www.raspberrypi-spy.co.uk/2012/11/how-to-rename-your-raspberry-pi/
Allerdings war unsere Fritz.box damit überfordert.
Fortan war es zielführender den Rechner via "192.168.5.47" statt "raspberrypi3" an zu sprechen. 

```bash
sudo vi /etc/network/interfaces
```

```bash
# interfaces(5) file used by ifup(8) and ifdown(8)

# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'

# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d

auto eth0

iface eth0 inet static
address 192.168.5.47
netmask 255.255.255.0
gateway 192.168.5.1
```

### Arduino IDE 1.8.5 auf dem Raspberry installieren

* Download Arduino IDE from www.arduino.cc. 
* Then unpack file.
* Dann:
```bash
rm Downloads/arduino-1.8.5-linuxarm.tar.xz
sudo mv Downloads/arduino-1.8.5/ /opt

# touch .xdg-icon-resource-dummy otherwise it is missing during install.sh
touch /home/pi/.local/share/icons/hicolor/.xdg-icon-resource-dummy
cd /opt/arduino-1.8.5/
./install.sh

lsusb

/opt/arduino-1.8.5/arduino
```
Der UNO wird erkannt uns lässt sich programmieren :-)


#### Auf dem Weg die Digistump Entwicklung auf Raspbian zu unterstützen

Im Prinzip: https://digistump.com/wiki/digispark/tutorials/connecting allerdings läuft das alles nicht auf dem raspberry.

```bash
sudo vi /etc/udev/rules.d/49-micronucleus.rules
#Und dieses einfügen: https://digistump.com/wiki/digispark/tutorials/linuxtroubleshooting

git clone https://github.com/micronucleus/micronucleus.git
cd micronucleus/commandline
sudo apt-get install libusb-dev # sonst wird beim make über usb.h gemeckert.
make
./micronucleus #test -> ok

mkdir -p /opt/arduino-1.8.5/hardware/digistump/avr/tools/
cp micronucleus /opt/arduino-1.8.5/hardware/digistump/avr/tools/

sudo /opt/arduino-1.8.5/arduino
```
Trotzdem meckert der Boardmanager über micronucleus :-(




