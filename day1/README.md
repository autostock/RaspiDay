Den "raspberrypi3" (mosquitto broker) umstellen auf feste IP Adresse
====
Wir fanden folgende Lösung. Allerdings war unsere Fritz.box damit überfordert.
Fortan war es zielführender den Rechner via "192.168.5.47" statt "raspberrypi3" an zu sprechen. 

```bash
vi /etc/network/interfaces
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

