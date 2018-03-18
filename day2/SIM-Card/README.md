# Arduino-Clone-Shield mit SIM900-Chip

Das Orginal wurde nicht mehr im Internet gefunden, aber ist ca.:
https://arduino-hannover.de/2014/04/20/mein-paket-ein-sim900-gsmgprs-shield/

Das Modul hängt direkt am UART vom Raspi. Ich hatte für Tx und Rx noch einen 3,3V-5V-Pegelwandler eingesetzt. 
Die AT-Befehle sind wohl weitgehend normiert, außer einigen speziellen für MMS. Das Modul hat die AT-Befehle
direkt verstanden.

Eine Besonderheit war, dass ich Tx und Rx nicht kreuzen musste/durfte, sondern Tx an Tx und Rx an Rx verbunden habe. 

