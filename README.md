# RaspiDay

Die Idee: Wir machen was mit MQTT auf dem Raspberry.


Im Szenario spielen 3 Raspberrys zusammen.

- Raspberry 1 dient als Eingabegerät. Hier werden einfache Ein/Aus-Schalter aber auch andere Sensoren angeschlossen (Temperatur, IR, Arduino, ...). Die Zustände der Schalter und Sensoren werden an den MQTT Server gesendet.

- Raspberry 2 dient als Ausgabegerät. Dort werden Sensorzustände vom MQTT Server abonniert und in Ausgaben verwandelt (LEDs, Piezo-Pieper, Servo, ...).

- Raspberry 3 ist der MQTT Server (MQTT Broker Mosquitto)


Optional:
- Raspberry 4 abonniert vom MQTT Server und visualisiert die Sensorzustände (https://plot.ly/python ?).


[[https://github.com/autostock/RaspiDay/blob/master/day1/20170924_161526.jpg]]
