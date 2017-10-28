Installiere MQTT auf raspberry
===
Ich habe mich für den mosquitto broker entschieden.
```bash
sudo apt-get update
sudo apt-get install mosquitto
sudo apt-get install mosquitto-clients
sudo apt-get install libmosquitto-dev # für Entwicklung
```
MQTT mosquitto testen
===
Terminal 1: mosquitto broker starten:
```bash
mosquitto
```
Terminal 2: mosquitto subscription client starten:
```bash
mosquitto_sub –t /sensor/test
```
Terminal 3: mosquitto public client starten:
```bash
mosquitto_pub –t /sensor/test –m "hello world"

```
Resultat: Im Terminal 2 erscheint ```hello world```

Installiere MQTT auf Windows 10 Home :-(
===
Das ist mir bisher nicht gelungen wg. Problemen mit der OpenSSH Komponente.
