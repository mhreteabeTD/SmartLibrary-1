import random
import time
import json
import paho.mqtt.publish as publish

while True:
    occupancy_count = random.randint(0,50)
    publish.single(
        "occupancy/sensor-data",
        json.dumps({"count":occupancy_count}),
        hostname="mosquitto"
    )
