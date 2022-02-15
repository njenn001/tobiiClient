import time 
from time import * 
import tobii_research as tr
from tobii_research import * 

class Tracker(): 
    def __init__(self, user):
        self.user = user
        self.tracker = None 
        self. name = None 
        self.gaze_callback = None 

        self.initialize()

    # GET / SET user 
    def get_user(self): 
        return self.user 
    def set_user(self, user):
        self.user = user 
    
    # GET / SET tracker 
    def get_tracker(self): 
        return self.tracker
    def set_tracker(self, tracker): 
        self.tracker = tracker

    # GET / SET name
    def get_name(self): 
        return self.name
    def set_name(self, name): 
        self.name = name 

    # GET / SET gaze callback 
    def get_callback(self): 
        return self.gaze_callback 
    def set_callback(self, callback): 
        self.gaze_callback = callback 


    # Initialize tracker & elements 
    def initialize(self): 
        self.set_tracker(tr.find_all_eyetrackers()[0])

    def get_points(self): 

        
        def gaze_data_callback(gaze_data):
            # Print gaze points of left and right eye
            print("Left eye: ({gaze_left_eye}) \t Right eye: ({gaze_right_eye})".format(
                gaze_left_eye=gaze_data['left_gaze_point_on_display_area'],
                gaze_right_eye=gaze_data['right_gaze_point_on_display_area']))

        while True:
            self.tracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
            sleep(5)