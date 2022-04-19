import os 
import tkinter 
import kafka

from tkinter import *
from kafka import * 

from tracker import Tracker 
from gaze import Gaze 

class Tester(kafka.KafkaProducer): 
    def __init__(self, controller):
        self.tracker = None
        self.gaze = None 
        self.controller = controller 

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

# GET / SET controller 
def get_controller(self): 
    return self.controller 
def set_controller(self, controller): 
    self.controller = controller  