import json
import paho.mqtt.client as mqtt
import time
from db_connection import *

#config
broker_address = "mosquitto"
port = 1883
topics =[
    "rfid/added",
    "rfid/removed"
]


connection = DBConnection()

def handle_book_added(payload):
    command="""INSERT INTO public.bookmanager_book_shelves (book_id, shelf_id) VALUES (%s, %s)"""
    try:
        msg=connection.cursor.execute(command,
                              (payload['book_id'], payload['shelf_id']))
        connection.conn.commit()
        print(f"successfuly added {payload['book_id']} to {payload['shelf_id']}",flush=True)
    except Exception as e:
        print(f'failure in handle_book_added: {e}',flush=True)
        connection.conn.reset()
    

def handle_book_removed(payload):
    command="""DELETE FROM public.bookmanager_book_shelves where  book_id = %s AND shelf_id=%s"""
    try:
        connection.cursor.execute(command,
                              (payload['book_id'], payload['shelf_id']))
        connection.conn.commit()
        print(f"successfuly removed {payload['book_id']} from {payload['shelf_id']}",flush=True)
    except Exception as e:
        print(f'failure in handle_book_removed: {e}',flush=True)
        connection.conn.reset()
    


def on_message(client,userdata,message):
    topic = message.topic
    payload=str(message.payload.decode("utf-8"))
    print(f"in {topic}")
    print(payload,flush=True)

    if topic == "rfid/added":
        handle_book_added(json.loads(payload))
        
    elif topic == "rfid/removed":
        handle_book_removed(json.loads(payload))
        

#create a new instance
client = mqtt.Client("rasberry-pi-client")

#connect to the broker
client.connect(broker_address,port=port)
client.on_message = on_message

#subscirbe to topics
for topic in topics:
    client.subscribe(topic)

#start the mqqt client
client.loop_forever()

