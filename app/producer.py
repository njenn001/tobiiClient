from kafka import *
from kafka import KafkaAdminClient  
from kafka.admin import * 
from tkinter import * 
import json
import time 
import threading
class Producer(KafkaAdminClient): 
    def __init__(self, user):
        self.user = user 
        self.args = None 
        
        # server info 
        self.bootstrap_server = '' 
        
        # topic info 
        self.topic_var = None 
        self.topic_name = '' 
        self.rep_fac = '' 
        self.num_par = '' 
        
        # message info 
        self.message = []
        
        # threads 
        self.key_thread = None 
        self.key_thread = threading.Thread(target=self.catch_key, args=([]))
        
    # Catch input key 
    def catch_key(self):
        if keyboard.is_pressed('q'):
            print() 
    
    # Decode existing args
    def decode_args(self): 
        
        self.bootstrap_server = self.args[0][0]
        
        super().__init__(bootstrap_servers=self.bootstrap_server)
        
        self.topic_name = self.args[1][0]
        self.message = self.args[2][0]    
    
    # Capture incoming Strict args 
    def strict(self, args): 
        self.args = args 
        self.decode_args() 
        
        try:
            self.send(self.topic_name, str(self.message).encode())
            time.sleep(5)
            print('sent')
        except Exception as ex: 
            print(ex) 

    # Describe a new message 
    def set_msg_descrip(self): 
        self.topic_name = self.user.controller.topic_entry.get()
        self.message = self.user.controller.message_entry.get('1.0', END).splitlines()
        
        self.user.controller.message_entry.delete('1.0', END)
        
    # Describe a new topic 
    def set_topic_descrip(self): 
        self.topic_name = self.user.controller.topic_entry.get()
        self.rep_fac = self.user.controller.rep_fac_entry.get() 
        self.num_par = self.user.controller.part_entry.get() 

        self.topic_var = NewTopic[(self.topic_name, self.rep_fac, self.num_par)]


    # Make a new topic   
    def make_topic(self): 
        super().__init__(bootstrap_servers=self.user.broker_id_str)
        try: 
            self.set_topic_descrip() 
            self.create_topics(self.topic_var, timeout_ms=None, validate_only=True)
        except Exception as ex: 
            self.user.throw_exec('c_t')
    # Send a message 
    def send_msg(self): 
        super().__init__(bootstrap_servers=self.user.broker_id_str)
         
        self.set_msg_descrip()
        self.send(self.topic_name, str(self.message[0]).encode())
        
        #self.poll(1)
