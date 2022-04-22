import os
from kafka import KafkaConsumer
from kafka import * 

import threading 

class Consumer(KafkaConsumer): 
    def __init__(self, user):
        self.user = user 
        self.args = None
         
        # topic info 
        self.topic_list = [] 
        self.topic_name = '' 

        # message info 
        self.messages = [] 
        
        # boolean 
        self.get = False 
        self.listen = False 
        self.exists = False 
        
        # thread info 
        self.threads = [] 
        self.show_thread = None  
        self.key_thread = None 

    # GET / SET user 
    def get_user(self): 
        return self.user
    def set_user(self, user): 
        self.user = user 

    # GET / SET args 
    def get_args(self): 
        return self.args 
    def set_args(self, args): 
        self.args = args 

    # GET / SET topic list 
    def get_topic_list(self): 
        return self.topic_list
    def set_topic_list(self, topic_list): 
        self.topic_list = topic_list

    # GET / SET get 
    def get_get(self): 
        return self.get
    def set_get(self, get): 
        self.get = get 

    # GET / SET exists 
    def get_exists(self): 
        return self.exists 
    def set_exists(self, exists): 
        self.exists = exists 
        
    # GET / SET / ADD thread 
    def get_threads(self): 
        return self.threads
    def set_threads(self, threads):
        self.threads = threads 
    def add_thread(self, thread):
        self.threads.append(thread) 
        
    # GET / SET key thread 
    def get_key_thread(self): 
        return self.key_thread
    def set_key_thread(self, thread): 
        self.key_thread = thread
        
    # Kill self
    def kill(self): 
        if self.get_exists(): 
            self.close() 
        #os.sys.exit()
        
    # Stop all threads 
    def stop_threads(self):
        try: 
            for t in self.get_threads():
                if not t.is_alive(): 
                    t.join() 
        except Exception as ex: 
            self.stop_threads()
        
    # Decode existing args
    def decode_args(self): 
        
        print(self.args[0][0])
        self.bootstrap_server = self.args[0][0]
        self.topic_name = self.args[1][0]
    
    # Describe a new topic 
    def set_topic_descrip(self): 
        self.topic_name = self.user.controller.topic_entry.get()

    # Get the topics at a broker 
    def get_topics(self): 
        try:
            super().__init__(bootstrap_servers=self.get_user().get_broker_str())

            if not self.topics(): 
                print('try again')
            else:     
                self.set_exists(True)
                self.set_topic_list(self.topics())
                print(self.get_user().get_consumer().topics())
                self.get_user().get_view().text_lines.config(state='normal')
                self.get_user().get_view().show_text(self.get_user().get_consumer().get_topic_list())
                self.get_user().get_view().text_lines.config(state='disabled')
                self.get_user().get_controller().reconfig('test_s')

        except Exception as ex: 
            
            self.get_user().throw_exec('test')    
            self.get_user().get_consumer().kill() 
            print(ex)


       
            

        