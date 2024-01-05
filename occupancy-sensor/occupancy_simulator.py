import random
import time
import json
import paho.mqtt.client as mqtt
from db_connection import *
from abc import ABC,abstractmethod


TIME_BETWEEN_READS = 10









class OccupancySensor(ABC):
    @abstractmethod
    def get_data(self):
        pass


class RealOccupancySensor(OccupancySensor):
    def get_data(self):
        pass



class SimulatedOccupancySensor(OccupancySensor):
    def __init__(self):
        self.connection = DBConnection()
        self.broker_address = "mosquitto"
        self.port = 1883
        self.topic ="occupancy/data"
        #create a new instance
        self.client = mqtt.Client("OccupancySensor")
        #connect to the broker
        self.client.connect(self.broker_address,port=self.port)
        self.client.loop_start()


    def get_data(self):
        #let's get a grid representation of our library
        cmd = """SELECT level_number FROM public.bookmanager_librarylevel ORDER BY id ASC """
        levels = self.connection.query(cmd)
        print(levels,flush=True)
        #then we can get generate a synthetic data based on that grid
        rows=7
        cols=7
        syntethic_data={"levels":[]}
        for level in levels:
            level_number = level[0]
            current_level_data={}
            syntethic_data['levels'].append(current_level_data)
            current_level_data['levelId'] = level_number
            current_level_data['gridData'] = [[0 for i in range(10)] for j in range(10)]
            for i in range(rows):
                for j in range(cols):
                    current_level_data['gridData'][i][j] = round(random.uniform(0,9))
        print(syntethic_data)
        return syntethic_data
    
    def publish_data(self,data):
        try:
            json_data = json.dumps(data)
            self.client.publish(topic=self.topic,payload=json_data)
            print('succesfuly published')
        except Exception as e:
            print(e,flush=True)

        







if __name__ == "__main__":
    sensor = SimulatedOccupancySensor()
    while True:
        data=sensor.get_data()
        sensor.publish_data(data)
        time.sleep(TIME_BETWEEN_READS)

    



