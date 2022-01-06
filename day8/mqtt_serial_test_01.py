#!/usr/bin/python3
# -*- coding: utf-8 -*-

# MQTT test application
# TODO: send Translated MQTT to Serial
# TODO: queue between Serial.read in case we want to publish
# TODO: communicate errors back over MQTT
#
# t1000 = 1000 ms
# 0 >= M1 >= 600        actually 20-980, extremes are not used, this program simply sends 1000
# 0 >= M2-6 >= 1000     actually 20-980, extremes are not used
# 
# xarm/set/direct =>	M1 M2 M3 M4 M5 M6       => s0 t1000 
#                                               => s1 p<M1> s2 p<M2> s3 p<M3> ... x
                                                    
#                       oder
#                                               => s1 p<M1> t1000 s2 t1000 p<M2> ... x
# xarm/set/timed  =>	M1 T1 M2 T2 M3 T3 M4 T4 M5 T5 M6 T6 => s1 p<M1> t<T1> s2 t1000 p<M2>  t<T1>... x
# xarm/set/time  =>	Tall  => t<Tall>
#                   example t1000  
# xarm/set/pos  =>	Pall  => t<Pall>
#                   example p1000  
# later:    xarm/set/pos  =>	max  => p<max>      # is 600 or 1000
# later:    xarm/set/pos  =>	min  => p<min>      # is 0
# xarm/set/testmode  =>	on      => T1       # test mode On
# xarm/set/testmode  =>	1       => T1       # test mode On
# xarm/set/testmode  =>	off     => T0       # test mode Off
# xarm/set/testmode  =>	0       => T0       # test mode Off

import paho.mqtt.client as mqtt
import threading
import queue
import serial
import sys
import time

defaultPos=0
defaultTime=1000
def translateMqttSerial(topic, value):
    global defaultTime, defaultPos
    #extract sub topic
    print("1. translateMqttSerial({}, {})".format(topic, value))
    if topic[:len("/xarm/set/")] != "/xarm/set/":
        print("2. translateMqttSerial({}, {}) ".format(topic, value))
        return "unknown command"
    print("3. translateMqttSerial({}, {}) ".format(topic, value))
    topic = topic[-(len(topic)-len("/xarm/set/")):]
    if topic[-1] == "/":
        topic=topic[:-1]
    #TODO: stub, remove when finisged
    #cmd = "{} msg={}".format(topic, value)
    cmd=""
    #check and translated base on topic
    if topic=="pos":
        #should have received one value
        try:
            defaultPos=int(value)
        except:
            defaultPos=0
        cmd="p{}".format(defaultPos)
    if topic=="time":
        #should have received one value
        try:
            defaultTime=int(value)
        except:
            defaultTime=1000
        cmd="t{}".format(defaultTime)
    if topic=="direct":
        #s1 p<M1> t1000 s2 t1000 p<M2> ... x
        # extract 6 values from value
        motors=value.split()
        if len(motors) == 6:
            cmd=""
            for i in range(len(motors)):
                cmd+= "s{} t{} p{} ".format(i+1, defaultTime, motors[i])
            cmd+= " x"
        else:
            print("nr of motor values incorrect")
    if topic=="timed":
        # xarm/set/timed  =>	M1 T1 M2 T2 M3 T3 M4 T4 M5 T5 M6 T6 => s1 p<M1> t<T1> s2 t<T2> p<M2> ... x
        posAndTime=value.split()
        if len(posAndTime) == 12:
            cmd=""
            for i in range(int(len(posAndTime)/2)):
                cmd+= "s{} t{} p{} ".format(i+1, posAndTime[i*2+1], posAndTime[i*2])
            cmd+= " x"
        else:
            print("nr of motor values incorrect: {} \m {}".format(len(posAndTime), posAndTime))
    return cmd

msgQ = queue.Queue() #no max_size
mqttQ = queue.Queue()

# topic="abc/"
# msg="was ich was"
# print("/translateMqttSerial({}, {}) = {}".format(topic, msg, translateMqttSerial(topic, msg)))
# topic="xarm/set/pos"
# msg="500"
# print("/translateMqttSerial({}, {}) = {}".format(topic, msg, translateMqttSerial(topic, msg)))
# topic="xarm/set/direct/"
# msg="0 100 200 300 400 500"
# print("/translateMqttSerial({}, {}) = {}".format(topic, msg, translateMqttSerial(topic, msg)))
# topic="xarm/set/timed/"
# msg="0 500 100 600 200 700 300 800 400 900 500 1100"
# print("/translateMqttSerial({}, {}) = {}".format(topic, msg, translateMqttSerial(topic, msg)))

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("MQTT: connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global msgQ
    topicTree = msg.topic.split('/')
#    print("on_message: MQTT:" + msg.topic +"["+str(len(topicTree))+"] payload: " + msg.payload.decode())
#    print("on_message: filter on {}".format(topicTree))
    if len(topicTree) > 1 and topicTree[1] == "xarm":
        print("on_message: MQTT: %s [%d] payload: %s" % (msg.topic , len(topicTree),  msg.payload.decode()) )
        if topicTree[2] in ['set', '']:
            cmd = translateMqttSerial(msg.topic, msg.payload.decode())
            if not cmd=="unknown command":
                print("msgQ.put_nowait : {}",format(cmd))
                msgQ.put_nowait("T0 "+cmd)

def startMQTT(name):
    print("Thead started: {}".format(name))
    #call as separate daemon thread
    global client
    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()

def mqttPublisher(name, q):
    global client
    #call as separate daemon thread
    print("Thead started: {}".format(name))
    while True:
        msg = q.get()
        if 'topic' in msg and 'msg' in msg:
            print("sending back using mqtt topic: {} val: {}".format(msg['topic'], msg['msg']))
            client.publish("/{}".format(msg['topic']), payload=msg['msg'])

#setup mqtt
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.178.31", 1883, 60)  # @Wolfgang

#client.loop_forever() # in a separate thread
#x=threading.Thread(target=startMQTT, args=(threading.get_ident(),), daemon=True)
mqttReader=threading.Thread(target=startMQTT, args=("mqtt Reader", ), daemon=True)
mqttReader.start()
mqttWriter=threading.Thread(target=mqttPublisher, args=("mqtt Writer",mqttQ, ), daemon=True)
mqttWriter.start()

#setup serial
def connect(port="/dev/ttyACM0", baudrate=115200, timeout=1):
    try:
        print("SERIAL: Connecting to Arduino on port:{} baudrate:{}...".format(port, baudrate))
        #ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)
        ser = serial.Serial(port, baudrate=baudrate)
        
        # The next line is necessary to give the firmware time to wake up.
        time.sleep(1)
        baud = ser.baudrate
        print("SERIAL: Connected at {}".format( baud))
        print("SERIAL: Arduino is ready.")
        return ser
    except Exception as e:
        print("SERIAL: Serial Exception: \n{}".format(e))
        return None
    
ser = connect()

seenPrompt=False
def readSerial(name,ser):
    global seenPrompt, mqttQ
    #call as separate daemon thread
    print("readSerial: Thead started: {}".format(name))
    while True:
        try:
            result = ser.readline().decode()
            if len(result) > 0:
                if result[0] == ">" and seenPrompt == False:
                    print("readSerial: seen prompt, deactivate testmode")
                    seenPrompt=True
                    msgQ.put_nowait('T0')
                    msgQ.put_nowait('s1 t1001 p900 s2 t1002 p530 s3 t1003 p500 s4 t1004 p900 s5 t1005 p500 s6 t10006 p800  x')
                if result[0] == 'd':
                    msgParts=result.split()
                    topic="xarm/sensor/dist/{}".format(msgParts[1])
                    msg = msgParts[2]
                    #TODO: write to queue or directly to MQTT
                    mqttQ.put_nowait({'topic': topic, 'msg': msg})

            print("readSerial: {}".format(result))
        except Exception as e:
            print("readSerial: Exception {}".format(e))

def writeSerialFromQueue(name, ser, q):
    #call as separate daemon thread
    print("Thead started: {}".format(name))
    while True:
        cmd = q.get()
        print("writeSerialFromQueue: {}".format(cmd))
        cmd = bytes(cmd + " \n", 'utf-8')
        ser.write(cmd)

#reader=threading.Thread(target=readSerial, args=(threading.get_ident(), ser, ), daemon=True)
if not ser is None:
    reader=threading.Thread(target=readSerial, args=("SERIAL Reader", ser, ), daemon=True)
    reader.start()
    writer=threading.Thread(target=writeSerialFromQueue, args=("SERIAL Reader", ser, msgQ ), daemon=True)
    writer.start()

cmd="start"
while cmd!="q":
    print("""
    Serial test as well
    s:"send this"
    r:read all and print
    """)
    cmd=input("next command and enter (q=quit)")
    if cmd=="r":
        ser.write(b'r\n')
    if cmd=="T0":
        #test modus aus
        ser.write(b'T0\n')
    if cmd=="T1":
        #test modus aus
        ser.write(b'T1\n')
    if cmd=="5":
        ser.write(b's0 t2000 p500 x')
    if cmd=="0":
        ser.write(b's0 t2000 p0 x')

print("SERIAL: closing")
if not ser is None:
    try:
        ser.close()
    except Exception as e:
        print("Serial: Exception {}".format(e))
