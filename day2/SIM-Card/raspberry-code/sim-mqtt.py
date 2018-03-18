# leitet SMS-Nachricht an MQTT-Broker weiter
# SIM-Modul an ttyS1
# Ansteuerung mit AT-Befehlen
# SMS-Format topic:payload
# initpin() einmal zu Beginn

import serial
import time
import paho.mqtt.client as mqtt

port=serial.Serial("/dev/ttyS1",9600)
#port.open()
client=mqtt.Client()
# MQTT-Server
client.connect("x.x.x.x",1883,60)

def initpin():
# SIM-PIN
  port.write("AT+CPIN=xxxx\r\n")
  out=''
  time.sleep(0.5)
  while port.inWaiting()>0:
    out+=port.read(1)
  print out

def readmsg1():
  port.write("AT+CMGR=1\r\n")
  out=''
  time.sleep(0.5)
  while port.inWaiting()>0:
    out+=port.read(1)
  if len(out)<7:
    print "keine Nachricht."
  else:
    print out
    nrstart=out.find('"+')
    nrend=out.find('"',nrstart+1)
    nr=out[nrstart+1:nrend]
    endline=out.find('\n',2)
    mess=out[endline+1:]
    endmess=mess.find('\n')-1
    mess=mess[:endmess]
# erlaubte Nummer
    if nr != "xxxxxxxxxxxxxx":
      print "ungueltige Nummer."
    else:
      print "Signal erhalten."
#      print "Message:"+mess
      endtopic=mess.find(':')
      topic=mess[:endtopic]
      payload=mess[endtopic+1:]
#      print "Topic:"+topic
#      print "Payload:"+payload
      client.publish(topic,payload)
    port.write('AT+CMGD=1\r\n')

while(1):
  readmsg1()
  time.sleep(10)

port.close()
