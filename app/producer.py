from kafka import *
from kafka import KafkaAdminClient  
from kafka.admin import * 
from tkinter import * 
import json
import time 
import threading
class Producer(KafkaProducer): 
    def __init__(self, user, *args):
        if len(args) > 0: 
            if isinstance(args[0], str) and isinstance(args[1], str): 
                # user info 
                self.user = user 
        
                # broker info 
                self.broker_str = args[0]
                self.topic_name = args[1]
                
                # message info  
                self.message = None
                
                # threads 

                super().__init__(bootstrap_servers=self.get_user().get_broker_str())
        
        else: 
            # user info 
                self.user = user 
        
                # broker info 
                self.broker_str = ''
                self.topic_name = ''
                
                # message info  
                self.message = None
                
                # threads 

        
    # GET / SET user 
    def get_user(self): 
        return self.user
    def set_user(self, user): 
        self.user = user 

    # GET / SET topic name 
    def get_topic_name(self): 
        return self.topic_name
    def set_topic_name(self, topic_name): 
        self.topic_name = topic_name

    # GET / SET broker str
    def get_broker_str(self): 
        return self.broker_str
    def set_broker_str(self, broker_str): 
        self.broker_str = broker_str

    # GET / SET messages 
    def get_message(self): 
        return self.message
    def set_message(self, message): 
        self.message = message 

    # Kill self
    def kill(self): 
        if self.get_exists(): 
            self.close() 
        #os.sys.exit()     

    # Capture incoming Strict args 
    def strict(self, args): 
        print()


    # Send a message 
    def send_msg(self): 
        
        self.send(self.get_topic_name(), self.get_message().encode('utf-8'))
        