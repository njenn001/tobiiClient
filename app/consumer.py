import os
from kafka import KafkaConsumer, KafkaClient
from kafka import * 

import threading 

class Consumer(KafkaConsumer): 
    def __init__(self, user):
        self.user = user 

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

    # GET / SET topic list 
    def get_topic_list(self): 
        return self.topic_list
    def set_topic_list(self, topic_list): 
        self.topic_list = topic_list

    # GET / SET topic name 
    def get_topic_name(self): 
        return self.topic_name
    def set_topic_name(self, topic_name): 
        self.topic_name = topic_name

    # GET / SET messages 
    def get_messages(self): 
        return self.messages 
    def set_messages(self, messages): 
        self.messages = messages 

    # ADD messages 
    def add_msg(self, msg): 
        self.get_messages().append(msg)

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

    # GET / SET show thread 
    def get_show_thread(self): 
        return self.show_thread
    def set_show_thread(self, show_thread): 
        self.show_thread = show_thread
        
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
    
    # Stricty consume a topics messages 
    def strict_messages(self): 
        self.set_get(True)
        try: 
            
            super().__init__(self.get_topic_name(), 
                bootstrap_servers=self.get_user().get_broker_str(), group_id=None, 
                auto_offset_reset='earliest', enable_auto_commit=False)
            
            self.subscribe(self.get_topic_name())
            for message in self: 
                #self.messages.append(m.value.decode())
                #print(message.value.decode(), end ="\n")      
                print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                        message.offset, message.key,
                                                        message.value))           
                
                #self.user.view.show_text(self.messages)
                if message.value.decode() == ' ' or message.value.decode() == '':
                    object.set_exists(False)
                    print("No more messages")
                    break 

        except Exception as ex: 

            self.get_user().throw_exec('strict')    
            self.get_user().get_consumer().kill() 
            print(ex)

    # Stricty consume a topics messages 
    def gui_messages(self): 
        
        self.get_user().get_view().clear_lines()
        
        super().__init__(self.get_topic_name(), 
            bootstrap_servers=self.get_user().get_broker_str(), group_id=None, 
            auto_offset_reset='earliest', enable_auto_commit=False)
        
        # Quick thread to display 
        def gui_show(object): 
            object.set_get(True)
        
            try: 
        
                object.subscribe(object.get_topic_name())
                for message in object: 
                    #object.messages.append(m.value.decode())
                    #print(message.value.decode(), end ="\n")      
                    if object.get_get(): 
                        object.set_exists(True)
                        object.add_msg(message.value.decode())
                        
                        # object.set_topic_list(object.topics())
                        object.get_user().get_view().text_lines.config(state='normal')
                        object.get_user().get_view().show_text(object.get_messages())
                        object.get_user().get_view().text_lines.config(state='disabled')
                        #object.get_user().set_test_status(True)
                        #object.get_user().get_controller().reconfig('test_s')

                        #object.user.view.show_text(object.messages)
                        if message.value.decode() == ' ' or message.value.decode() == '':
                            object.set_exists(False)
                            print("No more messages")
                            break 

            except Exception as ex: 

                object.get_user().throw_exec('gui')    
                object.get_user().get_consumer().kill() 
                print(ex)


        self.set_show_thread( threading.Thread(target=gui_show, args=([self])) ) 
        self.add_thread(self.get_show_thread())
        self.get_show_thread().start() 

    # Strictly consume all topics
    def strict_topics(self): 
        try:
            super().__init__(bootstrap_servers=self.get_user().get_broker_str())

            if not self.topics(): 
                print('try again')
            else:     
                self.set_exists(True)
                self.set_topic_list(self.topics())
                print(self.get_user().get_consumer().topics())
               
        except Exception as ex: 
            
            self.get_user().throw_exec('strict')    
            self.get_user().get_consumer().kill() 
            print(ex)

    # Get the topics at a broker 
    def gui_topics(self): 
        
        self.get_user().get_view().clear_lines()

        try:
            super().__init__(bootstrap_servers=self.get_user().get_broker_str())

            if not self.topics(): 
                print('try again')
            else:     
                self.set_exists(True)
                self.set_topic_list(self.topics())
                self.get_user().get_view().text_lines.config(state='normal')
                self.get_user().get_view().show_text(self.get_user().get_consumer().get_topic_list())
                self.get_user().get_view().text_lines.config(state='disabled')
                self.get_user().set_test_status(True)
                self.get_user().get_controller().reconfig('test_s')

        except Exception as ex: 

            self.set_exists(False)
            self.get_user().throw_exec('test')    
            self.get_user().get_consumer().kill() 
            print(ex)


       
            

        