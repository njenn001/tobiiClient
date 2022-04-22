import os 
from tkinter import *

from tracker import Tracker 
from gaze import Gaze 
from controller import Controller 
from view import View

class User(): 
    def __init__(self, *args):
        if len(args) > 0: 
            if isinstance(args[0], Controller): 
                self.tracker = None
                self.gaze = None 
                self.root = None 
                self.controller = args[0]
                self.view = None

                self.consumer = None 
                self.producer = None
                self.tester = None
                
                self.broker_id = ''
                self.broker_port = ''
                self.broker_str = '' 
            else: 
                self.tracker = None
                self.gaze = None 
                self.root = None 
                self.controller = None
                self.view = None

                self.consumer = None 
                self.producer = None 
                self.tester = None 

                self.broker_id = ''
                self.broker_port = ''
                self.broker_str = '' 
            

    # GET / SET tracker 
    def get_tracker(self): 
        return self.tracker 
    def set_tracker(self, tracker): 
        self.tracker = tracker 

    # GET / SET gaze
    def get_gaze(self): 
        return self.gaze
    def set_gaze(self, gaze): 
        self.gaze = gaze 
    
    # GET / SET root 
    def get_root(self): 
        return self.root
    def set_root(self, root):
        self.root = root 

    # GET / SET controller
    def get_controller(self): 
        return self.controller
    def set_controller(self, controller): 
        self.controller = controller 

    # GET / SET view 
    def get_view(self): 
        return self.view 
    def set_view(self, view): 
        self.view = view 

    # GET / SET consumer 
    def get_consumer(self): 
        return self.consumer
    def set_consumer(self, consumer): 
        self.consumer = consumer 

    # GET / SET producer 
    def get_producer(self): 
        return self.producer
    def set_producer(self, producer): 
        self.producer = producer 

    # GET / SET broker id 
    def get_broker_id(self): 
        return self.broker_id
    def set_broker_id(self, broker_id): 
        self.broker_id = broker_id

    # GET / SET broker port 
    def get_broker_port(self): 
        return str(self.broker_port)
    def set_broker_port(self, broker_port): 
        self.broker_port = broker_port 

    # GET / SET broker str
    def get_broker_str(self): 
        return self.broker_str
    def set_broker_str(self, broker_str): 
        self.broker_str = broker_str

    # Throw exception 
    def throw_exec(self, msg): 
        if msg == 'strict': 
            
            print("Failed run. Check parameters.")
             
            
        if msg == 'gui': 
            arr = ['Gui error', 'Ensure operating system compatability', 'Complete enviornment (nat or virt) setup', 'Try again']
            raise Exception(arr)
            
        
        if msg == 'test': 
            arr = ['Testing error', 'Check broker Ip address and port number', 'Ensure live Kafka elements', 'Try again']
            self.get_view().show_text(arr) 
            raise Exception(arr)
            
      
    # Run tkinter systems
    def gui(self): 

        def root_init(object): 
            if os.environ.get('DISPLAY','') == '':
                #print('no display found. Using :0.0')
                os.environ.__setitem__('DISPLAY', ':0.0')

            object.set_root(Tk())
            object.root.attributes('-topmost', True)
            object.root.title('Tobii Client')


        root_init(self)
        self.set_controller(Controller(self.get_root(), self))
        self.set_view(View(self.get_root(), self))

        self.root.mainloop()

    # Raw/Strict tracking          
    def run_strict(self, args):
        if args.bss and args.p: 