from tkinter import *
import os  
import threading
import time 

from tester import Tester 

class Controller(Frame): 

    def __init__(self, root, user):
        super().__init__()
        self.user = user
        self.root = root
        self.tester = None 

        # frames 
        self.button_frame = None
        self.input_frame = None
    
        # buttons 
        self.test_button = None
        self.start_button = None 
        self.stop_button = None 
        self.close_button = None 

        # titles 
        self.title = None 
        self.title_txt = 'Ensure Tracker connction'
        
        self.name_title = 'Name' 
        self.pin_title = 'Pin'
        self.host_title = 'Host' 
        self.port_title = 'Port'
        self.topic_title = 'Topic' 

        # entries 
        self.name_entry = None 
        self.pin_entry = None 
        self.host_entry = None
        self.port_entry = None  
        self.topic_entry = None 

        # boolean flags 
        self.stream_started = False
        self.test_started = False 

        # threads
        self.stream_thread = None
        self.stream_thread = None 

        # Controller Init 
        self.UIinit()

    # GET / SET user 
    def get_user(self): 
        return self.user 
    def set_user(self, user): 
        self.user = user 

    # GET / SET root 
    def get_root(self): 
        return self.root
    def set_root(self, root): 
        self.root = root

    # GET / SET tester 
    def get_tester(self): 
        return self.tester 
    def set_tester(self, tester): 
        self.tester = tester 

    # GET / SET button frame 
    def get_button_frame(self): 
        return self.button_frame
    def set_button_frame(self, button_frame): 
        self.button_frame = button_frame
    
    # GET / SET input frame 
    def get_input_frame(self): 
        return self.input_frame
    def set_input_frame(self, input_frame): 
        self.input_frame = input_frame 

    # GET / SET test button 
    def get_test_button(self): 
        return self.test_button
    def set_test_button(self, test_button): 
        self.test_button = test_button
        
    # GET / SET start button
    def get_start_button(self): 
        return self.start_button
    def set_start_button(self, start_button): 
        self.start_button = start_button
        
    # GET / SET stop button 
    def get_stop_button(self): 
        return self.stop_button
    def set_stop_button(self, stop_button): 
        self.stop_button = stop_button 
        
    # GET / SET close button 
    def get_close_button(self): 
        return self.close_button 
    def set_close_button(self, close_button): 
        self.close_button = close_button
            
    # GET / SET title 
    def get_title(self): 
        return self.title
    def set_title(self, title): 
        self.title = title
        
    # GET / SET title text 
    def get_title_txt(self): 
        return self.title_txt
    def set_title_txt(self, title_txt): 
        self.title_txt = title_txt 
        
    # GET / SET name entry
    def get_name_entry(self): 
        return self.name_entry.get()
    def set_name_entry(self, name_entry): 
        self.name_entry = name_entry

    # GET / SET pin entry 
    def get_pin_entry(self): 
        return self.pin_entry.get()
    def set_pin_entry(self, pin_entry): 
        self.pin_entry = pin_entry
        
    # GET / SET host entry
    def get_host_entry(self): 
        return self.host_entry.get()
    def set_host_entry(self, host_entry): 
        self.host_entry = host_entry
        
    # GET / SET port entry
    def get_port_entry(self): 
        return self.port_entry.get()
    def set_port_entry(self, port_entry): 
        self.port_entry = port_entry
        
    # GET / SET topic entry
    def get_topic_entry(self): 
        return self.topic_entry.get()
    def set_topic_entry(self, topic_entry): 
        self.topic_entry = topic_entry 
        
    # Reconfigure elements 
    def reconfig(self, conf_str): 
        
        if conf_str == 'init': 
            self.name_entry.config(state='disabled')
            self.pin_entry.config(state='disabled')
            self.host_entry.config(state='normal')
            self.port_entry.config(state='normal')
            self.topic_entry.config(state='disabled')  
        elif conf_str == 'test_s': 
            if self.get_user().get_test_status(): 
                self.name_entry.config(state='normal')
                self.pin_entry.config(state='normal')
                self.host_entry.config(state='disabled')
                self.port_entry.config(state='disabled')
                self.topic_entry.config(state='normal') 
                
                self.test_button.config(state='disabled')
                self.start_button.config(state='normal')
        elif conf_str == 'start':
            self.name_entry.config(state='disabled')
            self.pin_entry.config(state='disabled')
            self.host_entry.config(state='disabled')
            self.port_entry.config(state='disabled')
            self.topic_entry.config(state='disabled') 
            
            self.start_button.config(state='disabled')
            self.stop_button.config(state='normal')

        elif conf_str == 'stop':
            self.name_entry.config(state='disabled')
            self.pin_entry.config(state='disabled')
            self.host_entry.config(state='disabled')
            self.port_entry.config(state='disabled')
            self.topic_entry.config(state='normal') 
            
            self.start_button.config(state='normal')
            self.stop_button.config(state='disabled')

    # OS specific and shutdown TK 
    def close(self):
        self.get_root().destroy() 
        #os.sys.exit()

    # Init UI elements / abilities 
    def UIinit(self): 

        # OS specific and shutdown TK 
        def close(object):
            object.get_root().destroy() 
            os.sys.exit()
         
        # REWIRE THIS 
        # Start action_set or Send action 
        def start_send_seq(object): 

            self.get_user().get_consumer().kill()             
            self.get_user().init_tracker()
            self.get_user().get_tracker().start_tracking('gui')
            self.reconfig('start')
            
        # REWIRE THIS 
        # tracking / streaming threads 
        def stop_seq(object): 
            self.get_user().get_tracker().stop_tracking()

            self.reconfig('stop')
          
        # Perform tests before accessing other KAFKA elements 
        def test_seq(object): 

            self.get_user().set_broker_id(self.get_host_entry())
            self.get_user().set_broker_port(self.get_port_entry())

            some = self.get_user().get_broker_id() + ":" + self.get_user().get_broker_port()
            self.get_user().set_broker_str(some)

            self.set_tester(Tester(self.get_user()))
            self.get_tester().run()            
            
        # Initialize input frame  
        def init_input_frames(object): 
            
            
            # Focus into entry 
            def on_click(e): 
                
                if e.widget.cget('state') == 'normal': 
                   
                    if e.widget.get() == 'username': 
                        object.name_entry.delete(0,'end')
                        object.name_entry.insert(0, '')
                        object.name_entry.config(fg = 'black')

                    elif e.widget.get() == '000': 
                        object.pin_entry.delete(0,'end')
                        object.pin_entry.insert(0, '')
                        object.pin_entry.config(fg = 'black')

                    elif e.widget.get() == '0.0.0.0': 
                        object.host_entry.delete(0, 'end')
                        object.host_entry.insert(0, '')
                        object.host_entry.config(fg = 'black')
                    
                    elif e.widget.get() == '0000': 
                        object.port_entry.delete(0, 'end')
                        object.port_entry.insert(0, '')
                        object.port_entry.config(fg = 'black')
                    
                    elif e.widget.get() == 'main': 
                        object.topic_entry.delete(0, 'end')
                        object.topic_entry.insert(0, '')
                        object.topic_entry.config(fg = 'black')
                        
            # Focus away from name entry 
            def on_move_name(e): 
                if e.widget.cget('state') == 'normal': 
                    if e.widget.get() == '': 
                        object.name_entry.insert(0, 'username')
                        object.name_entry.config(fg='grey')        

            # Focus away from pin entry
            def on_move_pin(e): 
                if e.widget.cget('state') == 'normal': 
                    if e.widget.get() == '': 
                        object.pin_entry.insert(0, '000')
                        object.pin_entry.config(fg='grey')         
                                
            # Focus away from host entry 
            def on_move_host(e): 
                if e.widget.cget('state') == 'normal': 
                    if e.widget.get() == '': 
                        object.host_entry.insert(0, '0.0.0.0')
                        object.host_entry.config(fg='grey')
                        
            # Focus away from port entry 
            def on_move_port(e): 
                if e.widget.cget('state') == 'normal': 
                    if e.widget.get() == '': 
                        object.port_entry.insert(0, '0000')
                        object.port_entry.config(fg='grey')
                        
            # Focus away from topic entry 
            def on_move_topic(e): 
                if e.widget.cget('state') == 'normal': 
                    if e.widget.get() == '': 
                        object.topic_entry.insert(0, 'main')
                        object.topic_entry.config(fg='grey')
            
            # Bind entry actions 
            def bind_entries(object): 
                
                object.name_entry.bind('<FocusIn>', on_click)
                object.name_entry.bind('<FocusOut>', on_move_name)

                object.pin_entry.bind('<FocusIn>', on_click)
                object.pin_entry.bind('<FocusOut>', on_move_pin)

                object.host_entry.bind('<FocusIn>', on_click)
                object.host_entry.bind('<FocusOut>', on_move_host)
                
                object.port_entry.bind('<FocusIn>', on_click)
                object.port_entry.bind('<FocusOut>', on_move_port)
                
                object.topic_entry.bind('<FocusIn>', on_click)
                object.topic_entry.bind('<FocusOut>', on_move_topic)
                        
            # Pack entry elements onto UI 
            def pack_entries(object):

                object.name_title.grid(row=0, column=0)
                object.name_entry.grid(row=0, column=1) 
                object.pin_title.grid(row=1, column=0)
                object.pin_entry.grid(row=1, column=1)
                object.host_title.grid(row=2, column=0)
                object.host_entry.grid(row=2, column=1)
                object.port_title.grid(row=3, column=0)
                object.port_entry.grid(row=3, column=1)
                object.topic_title.grid(row=4, column=0)
                object.topic_entry.grid(row=4, column=1)                        
            
            # Init elements
            def init_elm(object):   
 
                # Insert example text 
                def insert_example(object): 
                    object.name_entry.insert(0, 'username')
                    object.pin_entry.insert(0, 'pin')
                    object.host_entry.insert(0, '0.0.0.0')
                    object.port_entry.insert(0, '0000')
                    object.topic_entry.insert(0, 'main')
            
                object.input_frame = Frame(object.root)
                object.input_frame.grid(row=0, column=1, pady=(25, 0))
                
                object.name_title = Label(object.input_frame, text="Username")
                object.pin_title = Label(object.input_frame, text="Pin")
                object.host_title = Label(object.input_frame, text="IP")
                object.port_title = Label(object.input_frame, text="Port")
                object.topic_title = Label(object.input_frame, text="Topic")
                
                object.name_entry = Entry(object.input_frame, foreground='grey')
                object.set_pin_entry( Entry(object.get_input_frame(), foreground='grey') )
                object.host_entry = Entry(object.input_frame, foreground='grey')
                object.port_entry = Entry(object.input_frame, foreground='grey')
                object.topic_entry = Entry(object.input_frame, foreground='grey')

                insert_example(object) 
                object.reconfig('init')
                        
            init_elm(object)
            pack_entries(object)
            bind_entries(object) 
                        
        # Initialize button frame 
        def init_button_frames(object):
            
            # Change button color on hover 
            def on_enter(e): 
                if e.widget.cget('state') == "normal":
                    if e.widget.cget("text") == 'Test':
                        object.test_button['background'] = 'light green'
                    elif e.widget.cget('text') == "Start/Send":
                        object.start_button['background'] = 'light green'
                    elif e.widget.cget("text") == 'Stop' :
                        object.stop_button['background'] = 'red'
                    elif e.widget.cget("text") == 'Close':
                        object.close_button['background'] = 'red'
                    
            # Change button color back 
            def on_leave(e): 
                if e.widget.cget("text") == 'Test':
                    object.test_button['background'] = 'white'
                elif e.widget.cget('text') == "Start/Send":
                    object.start_button['background'] = 'white'
                elif e.widget.cget("text") == 'Stop':
                    object.stop_button['background'] = 'white'
                elif e.widget.cget("text") == 'Close':
                    object.close_button['background'] = 'white' 
            
            # Bind button actions 
            def bind_buttons(object): 
                
                object.test_button.bind("<Enter>", on_enter)
                object.test_button.bind("<Leave>", on_leave)
                
                object.start_button.bind("<Enter>", on_enter)
                object.start_button.bind("<Leave>", on_leave)
                
                object.stop_button.bind("<Enter>", on_enter)
                object.stop_button.bind("<Leave>", on_leave)
                
                object.close_button.bind("<Enter>", on_enter)
                object.close_button.bind("<Leave>", on_leave)
                    
            # Pack buttons into UI 
            def pack_buttons(object):
                
                object.test_button.grid(row=1, column=0)
                object.start_button.grid(row=0, column=0)
                object.stop_button.grid(row=0, column=1)
                object.close_button.grid(row=1, column=1)
                
            # Init elements 
            def init_elm(object):
                object.button_frame = Frame(object.root, borderwidth=2, border=1)
                object.button_frame.grid(row=1, column=1, pady=(0,25), padx=(50,25))
                
                object.test_button = Button(object.button_frame, text="Test", command= lambda:test_seq(object), width=15, state='normal', bg = 'white')
                object.start_button = Button(object.button_frame, text="Start/Send", command= lambda:start_send_seq(object), width=15, state='disabled', bg = 'white')
                object.stop_button = Button(object.button_frame, text="Stop", command= lambda:stop_seq(object), width=15, state='disabled', bg = 'white')
                object.close_button = Button(object.button_frame, text="Close", command= lambda:close(object), width=15, state='normal', bg = 'white')
                
            init_elm(object)
            pack_buttons(object)            
            bind_buttons(object)
            
        init_button_frames(self)
        init_input_frames(self)
        