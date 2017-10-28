Ich  habe einen IR USB Stick für meinen raspberry. Wenn ich den einstecke und auf einer IR Fernbedienung eine Taste drücke liefert
```/dev/lirc0``` die empfangenen Impuls Timings:

```bash
od -t x4 -w4 -v /dev/lirc0
```
Resultat:
```
0000000 00ffffff
0000004 0100035f
0000010 00000392
0000014 01000392
0000020 0000035f
0000024 01000757
0000030 0000035f
0000034 01000392
0000040 0000035f
...
0000304 0100035f
0000310 00000724
0000314 01000392
...
```

Auch diese kann ich mittels mosquitto_pub, Zeile für Zeile versenden:
```bash
od -t x4 -w4 -v /dev/lirc0 | mosquitto_pub -t /sensor/lirc0 -l
```

So ein Tastendruck auf der IR Fernbedienung erzeugt viele Zeilen (im Beispiel oben sind es 205 Zeilen) und entsprechend Verkehr mit dem MQTT broker.
Um die Lage zu entspannen habe ich einen kleines C-Programm geschrieben (siehe ```c/timedflush.c```) welches
Bytes binär aus stdin liest, in Hex umwandelt und ein NL plus fflush sendet wenn stdin eine Pause von X ms macht.
Dann kann man wie folgt schreiben und hat nur eine Zeile und damit nur eine MQTT Message pro Tastendruck.
```bash
cat /dev/lirc0 | timedflush -t 180 | mosquitto_pub -t /sensor/lirc0 -l
```
Resultat:
```
ffffff009203000192030000f2060001920300005f0300019203000092030001920300005f0300019203000092030001920300005f0300019203000092030001920300005f030001920300005f0300019203000092030001920300005f0300012407000092030001
...
```

```timedflush``` läßt sich auf dem raspberry wie folgt compilieren:
```
g++ -o timedflush timedflush.c
```

Andere
===
```bash
cat /dev/lirc0 | ./timedflush  -t 180 | mosquitto_pub -t /sensor/lirc0 -l
cat /dev/input/by-id/usb-0402_ADC-joystick  | ./timedflush  -c 8 | mosquitto_pub -t /sensor/e-sky -l
cat /dev/input/by-id/usb-DragonRise_Inc._Generic_USB_Joystick-joystick | ./timedflush -c 8 | mosquitto_pub -t /sensor/joystick -l
cat /dev/midi1 | ./tr -c 18 -t 10 | mosquitto_pub -t /sensor/midi1 -l
```
