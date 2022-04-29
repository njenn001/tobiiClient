import os 
from tkinter import *

from tracker import Tracker 
from gaze import Gaze 
from controller import Controller
from view import View
from consumer import Consumer
from producer import Producer 


class User(): 
    def __init__(self, *args):
        if len(args) > 0: 
            if isinstance(args[0], Controller): 
                self.tracker = None
                self.gaze = None 
                self.gazes = [] 
                self.root = None 
                self.controller = args[0]
                self.view = None

                self.test_status = False

                self.consumer = None 
                self.producer = None
                self.client = None 
                
                self.broker_id = ''
                self.broker_port = ''
                self.broker_str = '' 
            else: 
                self.tracker = None
                self.gaze = None
                self.gazes = []  
                self.root = None 
                self.controller = None
                self.view = None

                self.test_status = False 

                self.consumer = None 
                self.producer = None 
                self.client = None 

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

    # GET / SET gazes 
    def get_gazes(self): 
        return self.gazes 
    def set_gazes(self, gazes): 
        self.gazes = gazes  

    # ADD gaze position 
    def add_gaze_position(self, gaze): 
        self.gazes.append(gaze)
    
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

    # GET / SET test status 
    def get_test_status(self):
        return self.test_status
    def set_test_status(self, test_status): 
        self.test_status = test_status

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

    # GET / SET client 
    def get_client(self): 
        return self.client 
    def set_client(self, client): 
        self.client = client 

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
    #
    # ------------------------------------------------------------------------------
    # Will throw an exception dependent on one of the follwing error(s) occuring: 
    # > Disfunctional parameters 
    # > Obj failure 
    #
    # ------------------------------------------------------------------------------
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


        if msg == 'topics': 
            arr = ['Broker topics may not exists', 'Create topic and try again'] 
            self.get_view().show_text(arr) 
            raise Exception(arr)
            
    # Initialize Tracking system
    #
    # ------------------------------------------------------------------------------
    # Will initialize the eye tracking equipment.  
    #
    # ------------------------------------------------------------------------------
    def init_tracker(self):
        self.set_tracker(Tracker(self)) 
      
    # Run GUI
    #
    # ------------------------------------------------------------------------------
    # Creates a Tkinter UI and serves to user.  
    # > Test broker existence/connectivity/content 
    # > Stream gaze data 
    #
    # ------------------------------------------------------------------------------
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

    # Strict production     
    #
    # ------------------------------------------------------------------------------
    # Begins strict production in the terminal. 
    # > Streams directly to specified broker
    # > Reliant on given topic 
    #
    # ------------------------------------------------------------------------------ 
    def strict_prod(self, args):
        if args.bss and args.topic:    
            self.set_broker_str(args.bss)     
            self.init_tracker() 
            self.get_tracker().start_tracking('strict', args.topic) 
        else: 
            
            self.throw_exec('strict')

    # Strict consumption      
    #
    # ------------------------------------------------------------------------------
    # Begins strict consumption  in the terminal. 
    # > Streams directly from specified broker
    # > Reliant on given topic/broker
    #
    # ------------------------------------------------------------------------------ 
    def strict_con(self, args):
        if args.bss:
            if not args.topic:
                self.set_broker_str(args.bss)
                self.set_consumer(Consumer(self))
                self.get_consumer().strict_topics()
            elif args.topic: 
                print(args.bss, args.topic)
                self.set_broker_str(args.bss[0])
                self.set_consumer(Consumer(self))
                self.get_consumer().set_topic_name(args.topic[0])
                self.get_consumer().strict_messages()
                self.get_consumer().kill()
            else: 
                self.throw_exec('strict')
        else: 
            self.throw_exec('strict')