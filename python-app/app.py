import paho.mqtt.client as mqtt
import time
#config
broker_address = "mosquitto"
port = 1883
topic ="test/topic"

#create a new instance
client = mqtt.Client("python-client")

#connect to the broker
client.connect(broker_address,port=port)
client.loop_start()


while 1:
    
    #publish a message
    result=client.publish(topic,"hello from the smart library team")

    time.sleep(10)