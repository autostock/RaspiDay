## MQTT Clients

### Arduino Yun

Ich  habe einen *Arduino Yun* den ich in das MQTT Szenario eingebunden habe.

Zunächst habe ich dazu *Adafruit_MQTT* eingesetzt.
(https://learn.adafruit.com/mqtt-adafruit-io-and-you/arduino-plus-library-setup).

Dies funktioniert zwar, aber hing vom WLAN "Wetter" ab. Denn es gab Zeiten
in denen die Verbindung grundlos abbrach. Dann wiederum ging 's auch
stundenlang gut. Allerdings bricht es schon bei leichtem Stress (zu viele Messages pro Zeiteinheit empfangen) gerne zusammen.

Daraufhin bin ich auf den *PubSubClient* Client umgestiegen (https://pubsubclient.knolleary.net/index.html).
Dazu musste ich ihn auf den Yun umstellen. Der läuft viel besser als *Adafruit_MQTT*.

Der Arduino Sketch *mqtt_basic* abonniert das Topic "/actor/linoino" und reagiert auf Messages mit den Inhalten "4", "5", ... oder "9" indem es die Farbe einer angeschlossenen LED Kette ändert.

### ESP-12

Auch der ESP-12 war im MQTT Szenario eingebunden.

Auf Basis des *PubSubClient* Clients "published" dieser Sketch die, via AD, gemessenen CO2 Werte in ppm auf das Topic "/sensor/CO2".
