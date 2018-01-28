# Gedächnisstütze für Nützliches

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
Des Folgende installiert leider nur die IDE Version 1.0.5.
```bash
sudo apt-get install arduino
```
Deshalb:
* Download Arduino IDE from www.arduino.cc. https://www.arduino.cc/en/Main/Software and select for "Linux ARM"
* Then unpack file.
* installieren und
* starten
Also:
```bash
tar -xvf Downloads/arduino-1.8.5-linuxarm.tar.xz
rm Downloads/arduino-1.8.5-linuxarm.tar.xz
sudo mv arduino-1.8.5/ /opt

# touch .xdg-icon-resource-dummy otherwise it is missing during install.sh
mkdir -p /home/pi/.local/share/icons/hicolor/
touch /home/pi/.local/share/icons/hicolor/.xdg-icon-resource-dummy
cd /opt/arduino-1.8.5/
./install.sh

#plugin the UNO and check it
lsusb

#start arduino
/opt/arduino-1.8.5/arduino
```
Der UNO wird erkannt uns lässt sich programmieren :-)


#### Auf dem Weg die Digistump Entwicklung auf Raspbian zu unterstützen

Im Prinzip: https://digistump.com/wiki/digispark/tutorials/connecting 
allerdings läuft das alles zunächst nicht auf dem raspberry.

Nach folgenden Anpassungen läuft es:
1. USB Devices vorbereiten.
2. micronucleus manuell für Raspbian compilieren.
3. Digistump Boardverwalter Datei änderen. (Keine Abhängigkeit von micronucleus mehr) 
4. In Digistump platform.txt eintragen wo der manuell compilierte micronucleus zu finden ist.

##### Im Einzelnen
###### USB Devices vorbereiten
```bash
sudo vi /etc/udev/rules.d/49-micronucleus.rules
#Und dieses einfügen: https://digistump.com/wiki/digispark/tutorials/linuxtroubleshooting
```

###### micronucleus manuell für Raspbian compilieren.
```bash
git clone https://github.com/micronucleus/micronucleus.git
cd micronucleus/commandline
sudo apt-get install libusb-dev # sonst wird beim make über usb.h gemeckert.
make
./micronucleus #test -> ok
```

###### Digistump Boardverwalter Datei änderen. (Keine Abhängigkeit von micronucleus mehr) 
Für Arduinos Boardverwalter darf nicht die Orginal Datei genommen werden.
Vielmehr muss sie manuell herunter geladen werden und dann
die Abhängigkeit vom micronucleus Tool gelöscht werden.
Denn das micronucleus Tool wird für den Raspberry offiziell nicht unterstützt. 
```bash
cd ~
wget http://digistump.com/package_digistump_index.json
ls -l package_digistump_index.json # test -> ok
```
Jetzt mit einem Editor die Datei */home/pi/package_digistump_index.json* öffnen.
Und die Abhängigkeit löschen. D.h. die folgenden Zeilen unter
*packages -> platforms -> Digistump AVR Boards -> toolsDependencies
löschen:
```bash
            },
            {
              "packager": "digistump",
              "name": "micronucleus",
              "version": "2.0a4"
```

Jetzt Arduino IDE starten und im Boardmanager obige Datei als
```bash
file:/home/pi/package_digistump_index.json
```
angeben und digispark Boards installieren.

Arduino wieder beenden.

###### In Digistump platform.txt eintragen wo der manuell compilierte micronucleus zu finden ist.
Jetzt sollte die Datei "/home/pi/.arduino15/packages/digistump/hardware/avr/1.6.7/platform.txt" 
existieren. Mit einem Editor öffnen und wie folgt anpassen:
```bash
...
# AVR Uploader/Programmers tools
# ------------------------------
...
###tools.micronucleus.cmd.path={runtime.tools.micronucleus.path}/launcher
# change to:
tools.micronucleus.cmd.path=/home/pi/micronucleus/commandline/micronucleus

...
###tools.micronucleus.upload.pattern="{cmd.path}" -cdigispark --timeout 60 -Uflash:w:{build.path}/{build.project_name}.hex:i
# change to:
tools.micronucleus.upload.pattern="{cmd.path}" -cdigispark --timeout 60 {build.path}/{build.project_name}.hex
...
```

```bash
/opt/arduino-1.8.5/arduino
```

Jetzt konnte ich den Digispark erfolgreich auf dem Raspberry programmieren. Zum Beispiel:
*Examples -> DigisparkCDC -> CDC_LED
oder
*Examples -> DigisparkCDC -> Echo


Leider funktioniert
*Examples -> DigisparkCDC -> Print
nicht. Da das Programm auf dem Digispark mit der Ausgabe startet bevor der 
serielle Monitor der Arduino IDE
die Verbindung hergestellt hat. Danach synchronisieren sich beide nicht mehr.
