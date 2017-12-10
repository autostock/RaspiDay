# RaspiDay2

Die Idee: Wir machen was mit MQTT und steuern Relais, Motoren, Ventilatoren, gehackte Akkuschrauber etc. und sogar Roboter.

Das Szenario im Kern wie gehabt: es spielen 3 Raspberrys zusammen. 
Allerdings geht es im Schwerpunkt, aber nicht ausschließlich, um Bewegliches: Relais, Motoren, Ventilatoren etc. und - wenn vorhanden - Roboter. 
Alle Kommandos werden über MQTT übermittelt. Auch - wo sinnvoll - über zwei Broker Hops (siehe Beispiel 2).

##Beispiel 1:
Ein Temperatursensor ist gekoppelt mit einem MQTT Client. 
Ein anderer MQTT Client hat den Sensor abonniert und schaltet bei zu hoher Temperatur einen Ventilator an. 
(Zusätzlich kann der Ventilator über eine IR Fernbedienung ein- und ausgeschaltet werden.)

##Beispiel 2:
Ein zweiter, unabhängiger Mosquitto Broker läuft in einem Raspberry (im Netz via WLAN) der einem Roboter steuert. 
Alle Robotersensoren und -aktoren vermitteln sich über diesen lokalen (und mobilen) Broker. 
Gleichzeitig kommuniziert dieser Broker mit dem stationären Broker.


![alt text](https://github.com/autostock/RaspiDay/blob/master/day2/Zeugs.jpg)
![alt text](https://github.com/autostock/RaspiDay/blob/master/day2/Robots.jpg)
