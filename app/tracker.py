import time 
from time import * 
import threading 
import tobii_research as tr
from tobii_research import * 

from gaze import Gaze
from producer import Producer 
from consumer import Consumer 

class Tracker(): 
    def __init__(self, user):
        self.user = user
        self.tracker = None 
        self. name = None 
        
        self.gaze_callback = None 
        self.tracking = False 

        # Threads 
        self.threads = []
        self.gaze_thread = None

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

    # GET / SET tracking 
    def get_tracking(self): 
        return self.tracking 
    def set_tracking(self, tracking): 
        self.tracking = tracking 

    # GET / SET threads 
    def get_threads(self): 
        return self.threads
    def set_threads(self, threads):
        self.threads = threads 
    
    # ADD thread 
    def add_thread(self, thread):
        self.threads.append(thread) 

    # GET / SET gaze thread 
    def get_gaze_thread(self): 
        return self.gaze_thread
    def set_gaze_thread(self, gaze_thread): 
        self.gaze_thread = gaze_thread

    # Stop all threads 
    def stop_threads(self):
        try: 
            for t in self.get_threads():
                if not t.is_alive(): 
                    t.join() 
        except Exception as ex: 
            self.stop_threads()

    # Initialize tracker & elements 
    def initialize(self): 
        self.set_tracker(tr.find_all_eyetrackers()[0])

    # Stop tracking sequence 
    def stop_tracking(self): 
        self.set_tracking(False)    
        self.get_user().get_consumer().set_get(False)
        self.stop_threads()    

    # Start tracking sequence 
    def start_tracking(self, str, *args): 
        if str == 'gui':
            self.set_tracking(True)
            self.get_user().set_producer(Producer(self.get_user(), self.get_user().get_broker_str(), self.get_user().get_controller().get_topic_entry() ))
            self.get_user().get_producer().set_topic_name(self.get_user().get_controller().get_topic_entry())
            self.get_user().set_consumer(Consumer(self.get_user()))
            self.get_user().get_consumer().set_topic_name(self.get_user().get_controller().get_topic_entry())
            self.get_user().get_consumer().gui_messages() 

            # Capture gaze 
            def capture_gaze(object):
                # Callback for tobii object 
                def gaze_data_callback(gaze_data):
                    
                    if object.get_tracking() is False: 
                        object.get_tracker().unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)

                    # Set gaze elements 
                    object.get_user().set_gaze(Gaze(object.get_user()))
                    object.get_user().get_gaze().set_l_x(gaze_data['left_gaze_point_on_display_area'][0])
                    object.get_user().get_gaze().set_l_y(gaze_data['left_gaze_point_on_display_area'][1])
                    object.get_user().get_gaze().set_r_x(gaze_data['right_gaze_point_on_display_area'][0])
                    object.get_user().get_gaze().set_r_y(gaze_data['right_gaze_point_on_display_area'][1])
                    object.get_user().get_gaze().set_l_mm(gaze_data['left_pupil_diameter'])
                    object.get_user().get_gaze().set_r_mm(gaze_data['right_pupil_diameter'])

                    #print(object.get_user().get_gaze().export_json())
                    object.get_user().get_producer().set_message(object.get_user().get_gaze().export_json())
                    object.get_user().get_producer().send_msg()


                #while self.get_tracking():
                object.get_tracker().subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
                sleep(5)               


            self.set_gaze_thread( threading.Thread(target=capture_gaze, args=([self])))
            self.add_thread(self.get_gaze_thread())
            self.get_gaze_thread().start()
        else: 
            
            if len(args[0][0]) > 0:  
                self.set_tracking(True)
                self.get_user().set_producer(Producer(self.get_user(), self.get_user().get_broker_str(), args[0][0]))
                self.get_user().get_producer().set_topic_name(args[0][0])
                self.get_user().set_consumer(Consumer(self.get_user()))
                self.get_user().get_consumer().set_topic_name(args[0][0])
                #self.get_user().get_consumer().strict_messages() 

                # Capture gaze 
                def capture_gaze(object):
                    # Callback for tobii object 
                    def gaze_data_callback(gaze_data):
                        
                        if object.get_tracking() is False: 
                            object.get_tracker().unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)

                        # Set gaze elements 
                        object.get_user().set_gaze(Gaze(object.get_user()))
                        object.get_user().get_gaze().set_l_x(gaze_data['left_gaze_point_on_display_area'][0])
                        object.get_user().get_gaze().set_l_y(gaze_data['left_gaze_point_on_display_area'][1])
                        object.get_user().get_gaze().set_r_x(gaze_data['right_gaze_point_on_display_area'][0])
                        object.get_user().get_gaze().set_r_y(gaze_data['right_gaze_point_on_display_area'][1])
                        object.get_user().get_gaze().set_l_mm(gaze_data['left_pupil_diameter'])
                        object.get_user().get_gaze().set_r_mm(gaze_data['right_pupil_diameter'])

                        print(object.get_user().get_gaze().export_json())
                        object.get_user().get_producer().set_message(object.get_user().get_gaze().export_json())
                        object.get_user().get_producer().send_msg()


                    #while self.get_tracking():
                    object.get_tracker().subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
                    sleep(5)               


                self.set_gaze_thread( threading.Thread(target=capture_gaze, args=([self])))
                self.add_thread(self.get_gaze_thread())
                self.get_gaze_thread().start()


