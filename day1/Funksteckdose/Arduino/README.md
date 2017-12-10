### Funksteckdose (433 MHz) mit Arduino UNO schalten
An dem UNO ist das "MX-05V 433MHz RF Funkmodul" angeschlossen.

#### renkforce
Der Sketch *RFSendMySwitchCode* nutzt die Arduino Library RCSwitch (https://github.com/sui77/rc-switch/). 
Mit diesem Code, wird meine Funksteckdose (Kanal 4; Adresse 3) für eine Sekunde eingeschaltet und danach wieder ausgeschaltet.

Am Besten hat das bei der Pulselänge 346 funktioniert.

#### Funksteckdosen von Conrad "Type Nr. RC 402 / GXA2867" aus dem Jahr 2000

http://www2.produktinfo.conrad.com/datenblaetter/450000-474999/464922-an-01-de-Funk_Schalt_Set.pdf

Der Sketch *remote1c* nutzt keine spezielle RF Library sonderen treibt den Pin 4 direkt in loop().
