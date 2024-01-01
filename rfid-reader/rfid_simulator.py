import random
import time
import json
import paho.mqtt.publish as publish

while True:
    simulated_tag_id =  random.randint(1000,9999)
    publish.single("rfid/sensor-data" , json.dumps({"tag_id":simulated_tag_id}), hostname="mosquitto")
    time.sleep(10)