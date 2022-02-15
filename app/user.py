import os 

from tracker import Tracker 

class User(): 
    def __init__(self):
        self.tracker = None
        self.gaze_position = [] 

    # Throw exception 
    def throw_exec(self, msg): 
        if msg == 'r': 
            raise Exception("Failed run")
      
        
    # Run tkinter systems         
    def run(self):
        self.tracker = Tracker(self) 
        
        self.tracker.get_points()