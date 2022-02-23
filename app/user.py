import os 
from tkinter import *

from tracker import Tracker 
from gaze import Gaze 
from controller import Controller 

class User(): 
    def __init__(self):
        self.tracker = None
        self.gaze = None 
        self.root = None 
        self.controller = None 

    # GET / SET tracker 
    def get_tracker(self): 
        return self.tracker
    # GET / SET gaze
    def set_tracker(self, tracker): 
        self.tracker = tracker 
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

    # Throw exception 
    def throw_exec(self, msg): 
        if msg == 'r': 
            raise Exception("Failed run. Check parameters.")
        if msg == 'gui': 
            raise Exception("Environment can not support GUI.")
      
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
        self.set_controller(Controller(self.root, self))

        self.root.mainloop()

        
    # Raw/Strict tracking          
    def run_strict(self):
        self.tracker = Tracker(self) 
        
        self.tracker.get_points()