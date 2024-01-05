import random
import time
import json
import paho.mqtt.client as mqtt
from db_connection import *


class RFIDReaderInterface:
    def read_tags(self):
        raise NotImplementedError
    

class RealRFIDReader(RFIDReaderInterface):
    def read_tags(self):
        pass



class SimulatedRFIDReader(RFIDReaderInterface):
    def __init__(self):
        self.connection = DBConnection()
        self.broker_address = "mosquitto"
        self.port = 1883
        self.on_add_topic ="rfid/added"
        self.on_remove_topic ="rfid/removed"
        #create a new instance
        self.client = mqtt.Client("RFIDReader")
        #connect to the broker
        self.client.connect(self.broker_address,port=self.port)
        self.client.loop_start()

        #list to store books that are of the shelve
        self.off_shelve_books=[]
        self.shelf_choices=list(self.connection.query("SELECT s.id FROM public.bookmanager_shelf as s"))

        #some variables which would be useful for the simulation
        self.PROBABLITY_OF_BOOK_REMOVAL=0.5
        self.PROBABLITY_OF_BOOK_RETURN=0.5


    def on_add_to_shelf(self,data):
        
        json_data = json.dumps(data)
        try:
            info=self.client.publish(self.on_add_topic , json_data)
            print("in add",info,data,flush=True)
        except:
            print("in add",info,data,flush=True)
    
    
    def on_remove_from_shelf(self,data):
        json_data = json.dumps(data)
        try:
            info=self.client.publish(self.on_remove_topic , json_data)
            print("in remove",info,data,flush=True)
        except:
            print("in remove",info,data,flush=True)






    
    def read_tags(self):
        cmd="""
    SELECT s.id, s.shelf_number, s.description, b.id, b.title, b.author, b.rating
    FROM public.bookmanager_shelf AS s
    LEFT JOIN public.bookmanager_book_shelves AS bs ON s.id = bs.shelf_id
    LEFT JOIN public.bookmanager_book AS b ON bs.book_id = b.id
    ORDER BY s.id, b.id
"""    
        result = self.connection.query(cmd)
        
        #in here we are gone check books which are onthe shelve and remove some of them
        for row in result:
            shelf_id, shelf_number, shelf_description, book_id, book_title, book_author, book_rating = row
            print(f'book {book_title} on shelf {shelf_number}',flush=True)
            print(type(book_title),flush=True)
            x=random.random()
            data={
                "shelf_id":shelf_id,
                "shelf_number":shelf_number,
                "book_id":book_id,
                "book_title":book_title
            }
            #let's check that this books isn't already removed
            if book_id in self.off_shelve_books or book_id==None:
                continue

            if  x <= self.PROBABLITY_OF_BOOK_REMOVAL:
                self.on_remove_from_shelf(data)
                self.off_shelve_books.append(book_id)
        
        #now let's take the books that are off shelve and try to return some of them
        for book_id in self.off_shelve_books:
            x = random.random()
            if x <= self.PROBABLITY_OF_BOOK_RETURN:
                shelf_id=random.choice(self.shelf_choices)[0]
                data={
                    'book_id':book_id,
                    'shelf_id':shelf_id
                }
                command="""SELECT FROM public.bookmanager_book_shelves where  book_id = %s AND shelf_id=%s"""
                result=self.connection.cursor.execute(command,
                              (book_id, shelf_id))
                if not result:
                    self.on_add_to_shelf(data)
                    self.off_shelve_books.remove(book_id)
                

                


        


        




if __name__ == "__main__":
    rfid_reader=SimulatedRFIDReader()

    while True:
        #now we can decide how frequently we want to access our readers
        TIME_BETWEEN_READS=10
        rfid_reader.read_tags()
        time.sleep(TIME_BETWEEN_READS)
        
