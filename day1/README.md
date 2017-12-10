# RaspiDay1

Die Idee: Wir machen was mit MQTT auf dem Raspberry.


Im Szenario spielen 3 Raspberrys zusammen.

- Raspberry 1 dient als Eingabegerät. Hier werden einfache Ein/Aus-Schalter aber auch andere Sensoren angeschlossen (Temperatur, IR, Arduino, ...). Die Zustände der Schalter und Sensoren werden an den MQTT Server gesendet.

- Raspberry 2 dient als Ausgabegerät. Dort werden Sensorzustände vom MQTT Server abonniert und in Ausgaben verwandelt (LEDs, Piezo-Pieper, Servo, ...).

- Raspberry 3 ist der MQTT Server (MQTT Broker Mosquitto)


Optional:
- Raspberry 4 abonniert vom MQTT Server und visualisiert die Sensorzustände (https://plot.ly/python ?).

## Hilfreiche Links

- Generell: gute Übersicht über alle möglichen Raspi-Themen: https://www.elektronik-kompendium.de/sites/raspberry-pi/2011121.htm
- php7 und lighttpd: https://www.kohta-pi.de/2017/03/12/raspberry-pi-webserver-einrichten/#PHP_installieren
- http://www.instructables.com/id/Installing-MQTT-BrokerMosquitto-on-Raspberry-Pi/
- http://kevinboone.net/mosquitto-test.html
- https://pubsubclient.knolleary.net/index.html
- https://mosquitto.org
- https://mosquitto.org/man/mqtt-7.html
- http://www.eclipse.org/paho
- http://wiki.eclipse.org/Paho
- https://github.com/eclipse/paho.mqtt.java

![alt text](https://github.com/autostock/RaspiDay/blob/master/day1/20170924_161526.jpg)
