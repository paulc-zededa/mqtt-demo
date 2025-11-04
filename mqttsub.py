#!/usr/bin/env python3

import paho.mqtt.client as mqttClient
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        client.subscribe("sensors")
    
    else:
        print("Connection failed")

def on_message(client, userdata, message):
    print("Message received : "  + str(message.payload) + " on " + message.topic)


broker_address= "0.0.0.0"          
port = 9002                          

client = mqttClient.Client(mqttClient.CallbackAPIVersion.VERSION1)          
client.username_pw_set("", "")
client.on_connect= on_connect    
client.on_message= on_message        
client.connect(broker_address, port=port)     
client.loop_start()


try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()

