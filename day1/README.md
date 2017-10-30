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

### Den "raspberrypi3" (mosquitto broker) umstellen auf feste IP Adresse
Wir fanden folgende Lösung. Allerdings war unsere Fritz.box damit überfordert.
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
