import os 
import tkinter 

from tkinter import *

from consumer import Consumer

class Tester(): 
    def __init__(self, user):
        self.user = user
        self.test_status = False

    # GET / SET user 
    def get_user(self): 
        return self.user 
    def set_user(self, user): 
        self.user = user 

    # GET / SET test status 
    def get_test_status(self):
        return self.test_status
    def set_test_status(self, test_status): 
        self.test_status = test_status

    # Run test sequence 
    def run(self): 

        self.get_user().set_consumer(Consumer(self.get_user()))
        self.get_user().get_consumer().get_topics()