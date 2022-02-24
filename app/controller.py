from tkinter import *
import os  
import threading
import time 

class Controller(Frame): 

    def __init__(self, root, user):
        self.user = user
        super().__init__()
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
        self.host_title = 'Host' 
        self.port_title = 'Port'
        self.topic_title = 'Topic' 

        # entries 
        self.name_entry = None 
        self.host_entry = None
        self.port_entry = None  
        self.topic_entry = None 

        # boolean flags 
        self.stream_started = False
        self.test_started = False 

        # threads
        self.stream_thread = None

        # Controller Init 
        self.UIinit()
    
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
        return self.name_entry
    def set_name_entry(self, name_entry): 
        self.name_entry = name_entry
        
    # GET / SET host entry
    def get_host_entry(self): 
        return self.host_entry
    def set_host_entry(self, host_entry): 
        self.host_entry = host_entry
        
    # GET / SET port entry
    def get_port_entry(self): 
        return self.port_entry
    def set_port_entry(self, port_entry): 
        self.port_entry = port_entry
        
    # GET / SET topic entry
    def get_topic_entry(self): 
        return self.topic_entry
    def set_topic_entry(self, topic_entry): 
        self.topic_entry = topic_entry 
        
    # Reconfigure button elements 
    def reconfig(self, conf_str): 
        
        if conf_str == 'init': 
            self.host_entry.config(state='normal')
            self.port_entry.config(state='normal')
            self.topic_entry.config(state='disabled')
            self.message_entry.config(state='disabled')
            self.rep_fac_entry.config(state='disabled')
            self.part_entry.config(state='disabled')
                   
        '''def enable(children): 
            for c in children: 
                c.configure(state='normal')
        
        def disable(children): 
            for c in children: 
                c.configure(state='disabled')'''
    
    
    # Init UI elements / abilities 
    def UIinit(self): 
         
        # OS specific and shutdown TK 
        def close(object):
            object.root.destroy() 
            os.sys.exit()
            

        # Clear message lines 
        def clear_msg(object): 
            self.message_entry.delete('1.0', END)
        
        # Start action_set or Send action 
        def start_send_seq(object): 
            
            # Message thread 
            def message_thread(object): 
                object.user.producer = Producer(object.user)

                try: 
                    object.user.producer.send_msg() 
                    time.sleep(5)     
                    object.user.producer.close()
                    
                    object.get_thread = threading.Thread(target=get_thread, args=([object]))
                    object.get_thread.start() 
                    
                    object.user.status_bar.refresh_action(TRUE)
                    
                    
                except Exception as ex: 
                
                    self.user.status_bar.refresh_action(FALSE)

                    print(ex)
              
             # Get thread       
            def get_thread(object): 
                object.user.consumer = Consumer(object.user)
                
                try: 
                    object.user.consumer.get = True 
                    object.user.consumer.get_msgs()
                    time.sleep(5)
                    
                    object.user.status_bar.refresh_action(TRUE)
                        
                except Exception as ex: 
                
                    self.user.status_bar.refresh_action(FALSE)

                    print(ex)   
                    
            # Topic thread 
            def topic_thread(object): 
                object.user.producer = Producer(object.user)
                
                try: 
                    object.user.producer.make_topic()
                    time.sleep(5)
                    
                    object.user.status_bar.refresh_action(TRUE)
                        
                except Exception as ex: 
                
                    self.user.status_bar.refresh_action(FALSE)

                    print(ex)   
            
            # Send new Topic 
            if object.topic_started: 
                object.user.producer = Producer(object.user)
            
                try: 
                    object.topic_thread = threading.Thread(target=message_thread, args=([object]))
                    object.topic_thread.start() 
                    
                except Exception as ex: 
                    print(ex)

                object.topic_started = False 
            
            # Send Message 
            elif object.msg_started: 
                
                try: 

                    object.msg_thread = threading.Thread(target=message_thread, args=([object]))
                    object.msg_thread.start() 
                    
                except Exception as ex: 
                    print(ex) 
                
                object.msg_started = False 
                #object.topic_entry.delete(0, 'end')

            # Get Messages once 
            elif object.get_started: 
                
                try : 
                    
                    object.get_thread = threading.Thread(target=get_thread, args=([object]))
                    object.get_thread.start()
                    
                except Exception as ex:                    
                    print(ex)
                
                object.get_started = False 

        # REWIRE THIS 
        # End address:port designation 
        def stop_seq(object): 
            
            self.host_entry.delete(0, END)
            self.port_entry.delete(0, END)
            # self.topic_entry.delete(0, END)
            # Figure out how to empty this self.message_entry.delete(0, END)
            self.rep_fac_entry.delete(0, END)
            self.part_entry.delete(0, END)
                        
            self.host_entry.config(state='normal')
            self.port_entry.config(state='normal')
            self.topic_entry.config(state='disabled')
            # Figure out how to empty this self.message_entry.config(state='disabled')
            self.rep_fac_entry.config(state='disabled')
            self.part_entry.config(state='disabled')
            
            
            self.stop_button.config(state='disabled')
            self.start_button.config(state='disabled')
            self.topic_button.config(state='disabled')
            self.topics_button.config(state='disabled')
            self.message_button.config(state='disabled')
            self.stream_button.config(state='disabled')
            self.get_button.config(state='disabled')
            self.listen_button.config(state='disabled')
            
            self.test_button.config(state='normal')
            self.close_button.config(state='normal')
            
            if self.user.producer is not None: 
                
                print() 
                self.user.producer = None 
                
                #self.msg_thread.join()  
            if self.user.consumer is not None: 
                
                #self.get_thread.join()  
                
                self.user.consumer.get = False 
                self.user.consumer = None 
                    
          
        # Begin get sequence 
        def get_seq(object):

            self.get_started = True 

            self.host_entry.config(state='disabled')
            self.port_entry.config(state='disabled')
            self.test_button.config(state='disabled')
            self.close_button.config(state='disabled')       
            self.topic_button.config(state='disabled')
            self.topics_button.config(state='disabled') 
            self.message_button.config(state='disabled')
            self.stream_button.config(state='disabled')
            self.get_button.config(state='disabled')
            self.listen_button.config(state='disabled')
            self.rep_fac_entry.config(state='disabled')
            self.part_entry.config(state='disabled') 
            
            self.message_entry.config(state='disabled')
            self.start_button.config(state='normal')
            self.stop_button.config(state='normal')
            self.topic_entry.config(state='normal')

            print() 

        # WORK ON THIS 
        # Begin message sequence 
        def msg_seq(object): 
            self.msg_started = True
            
            self.host_entry.config(state='disabled')
            self.port_entry.config(state='disabled')
            self.test_button.config(state='disabled')
            self.close_button.config(state='disabled')       
            self.topic_button.config(state='disabled')
            self.topics_button.config(state='disabled') 
            self.message_button.config(state='disabled')
            self.stream_button.config(state='disabled')
            self.get_button.config(state='disabled')
            self.listen_button.config(state='disabled')
            self.rep_fac_entry.config(state='disabled')
            self.part_entry.config(state='disabled') 
            
            self.message_entry.config(state='normal')
            self.start_button.config(state='normal')
            self.stop_button.config(state='normal')
            self.topic_entry.config(state='normal')

            print() 

        # WORK ON THIS 
        # Begin topic sequence 
        def topic_seq(object): 
            self.topic_started = True
            
            self.host_entry.config(state='disabled')
            self.port_entry.config(state='disabled')
            self.test_button.config(state='disabled')
            self.close_button.config(state='disabled')       
            self.topic_button.config(state='disabled')
            self.topics_button.config(state='disabled') 
            self.message_button.config(state='disabled')
            self.stream_button.config(state='disabled')
            self.get_button.config(state='disabled')
            self.listen_button.config(state='disabled')
            self.message_entry.config(state='disabled')

            self.start_button.config(state='normal')
            self.stop_button.config(state='normal')
            self.topic_entry.config(state='normal')
            self.rep_fac_entry.config(state='normal')
            self.part_entry.config(state='normal')

            print() 

        # WORK ON THIS 
        # Begin topic(s) sequence
        def topics_seq(object): 
            print() 

            
        # Perform tests before accessing other KAFKA elements 
        def test_seq(object): 
            
            object.tester = Tester(object.user)
            object.tester.run() 
            
            pass
        
        # Initialize input frame  
        def init_input_frames(object): 
            
            
            # Focus into entry 
            def on_click(e): 
                if e.widget.cget('state') == 'normal': 
                    if e.widget.get() == '0.0.0.0': 
                        object.host_entry.delete(0, 'end')
                        object.host_entry.insert(0, '')
                        object.host_entry.config(fg = 'black')
                    elif e.widget.get() == '0000': 
                        object.port_entry.delete(0, 'end')
                        object.port_entry.insert(0, '')
                        object.port_entry.config(fg = 'black')
                    elif e.widget.get() == 'Dictionary': 
                        object.topic_entry.delete(0, 'end')
                        object.topic_entry.insert(0, '')
                        object.topic_entry.config(fg = 'black')
                    elif e.widget.get() == '1': 
                        object.rep_fac_entry.delete(0, 'end')
                        object.rep_fac_entry.insert(0, '')
                        object.rep_fac_entry.config(fg = 'black')
                    elif e.widget.get() == '2': 
                        object.part_entry.delete(0, 'end')
                        object.part_entry.insert(0, '')
                        object.part_entry.config(fg = 'black')  
                        
            # Focus into message 
            def on_click_msg(e):
                msg = '' 
                lines = self.message_entry.get('1.0', END).splitlines() 
                for l in lines: 
                    msg += msg + str(l)
                    
                if msg.replace(' ', '') == 'Wordoftheday!':
                    clear_msg(object)    
                    
                object.message_entry.config(fg='black')
                        
                                     
                                
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
                        object.topic_entry.insert(0, 'Dictionary')
                        object.topic_entry.config(fg='grey')
            
            # WORK ON THIS        
            # Focus away from message entry 
            def on_move_msg(e): 
                if e.widget.cget('state') == 'normal': 
                    
                    msg = '' 
                    lines = self.message_entry.get('1.0', END).splitlines() 
                    for l in lines: 
                        msg += msg + str(l)
                        
                    if msg.replace(' ', '') == '': 
                        object.message_entry.insert('1.0', 'Word of the day!')
                        object.message_entry.config(fg='grey')
                        
            # Focus away from rep fac entry 
            def on_move_rep(e): 
                if e.widget.cget('state') == 'normal': 
                    if e.widget.get() == '': 
                        object.rep_fac_entry.insert(0, '1')
                        object.rep_fac_entry.config(fg='grey')
                        
            # Focus away from part entry 
            def on_move_part(e): 
                if e.widget.cget('state') == 'normal': 
                    if e.widget.get() == '': 
                        object.part_entry.insert(0, '2')
                        object.part_entry.config(fg='grey')
                        
            
            # Bind entry actions 
            def bind_entries(object): 
                object.host_entry.bind('<FocusIn>', on_click)
                object.host_entry.bind('<FocusOut>', on_move_host)
                
                object.port_entry.bind('<FocusIn>', on_click)
                object.port_entry.bind('<FocusOut>', on_move_port)
                
                object.topic_entry.bind('<FocusIn>', on_click)
                object.topic_entry.bind('<FocusOut>', on_move_topic)
                
                object.message_entry.bind('<FocusIn>', on_click_msg)
                object.message_entry.bind('<FocusOut>', on_move_msg)

                object.rep_fac_entry.bind('<FocusIn>', on_click)
                object.rep_fac_entry.bind('<FocusOut>', on_move_rep)
                
                object.part_entry.bind('<FocusIn>', on_click)
                object.part_entry.bind('<FocusOut>', on_move_part)
            
            
            # Pack entry elements onto UI 
            def pack_entries(object):
                object.host_title.grid(row=1, column=0)
                object.host_entry.grid(row=1, column=1, columnspan=14)
                object.port_title.grid(row=2, column=0)
                object.port_entry.grid(row=2, column=1)
                object.topic_title.grid(row=3, column=0)
                object.topic_entry.grid(row=3, column=1)
                object.message_title.grid(row=4, column=0)
                object.message_entry.grid(row=4, column=1)
                object.rep_fac_title.grid(row=5, column=0)
                object.rep_fac_entry.grid(row=5, column=1)
                object.part_title.grid(row=6, column=0)
                object.part_entry.grid(row=6, column=1) 
                        
            
            # Init elements
            def init_elm(object):   
                
                
                # Insert example text 
                def insert_example(object): 
                    object.host_entry.insert(0, '0.0.0.0')
                    object.port_entry.insert(0, '0000')
                    object.topic_entry.insert(0, 'Dictionary')
                    object.message_entry.insert(END,'Word of the day!') 
                    object.rep_fac_entry.insert(0, '1')
                    object.part_entry.insert(0, '2')
            
                object.input_frame = Frame(object.root)
                object.input_frame.grid(row=1, column=1, rowspan=15)
                
                object.host_title = Label(object.input_frame, text="HOST IP")
                object.port_title = Label(object.input_frame, text="PORT")
                object.topic_title = Label(object.input_frame, text="TOPIC")
                object.message_title = Label(object.input_frame, text="MESSAGE")
                object.rep_fac_title = Label(object.input_frame, text="REP. FACTOR")
                object.part_title = Label(object.input_frame, text="NUM. PARTITIONS")
                
                object.host_entry = Entry(object.input_frame, foreground='grey')
                object.port_entry = Entry(object.input_frame, foreground='grey')
                object.topic_entry = Entry(object.input_frame, foreground='grey')
                object.message_entry = Text(object.input_frame, foreground='grey', width=15, height=5)
                object.rep_fac_entry = Entry(object.input_frame, foreground='grey')
                object.part_entry = Entry(object.input_frame, foreground='grey')
                
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
                    elif e.widget.cget('text') == 'New Topic': 
                        object.topic_button['background'] = 'yellow'
                    elif e.widget.cget('text') == 'Topics': 
                        object.topics_button['background'] = 'yellow'
                    elif e.widget.cget('text') == 'Message': 
                        object.message_button['background'] = 'yellow'
                    elif e.widget.cget('text') == 'Stream': 
                        object.stream_button['background'] = 'yellow'
                    elif e.widget.cget('text') == 'Get': 
                        object.get_button['background'] = 'yellow'
                    elif e.widget.cget('text') == 'Listen': 
                        object.listen_button['background'] = 'yellow'
                        
                    
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
                elif e.widget.cget('text') == 'New Topic': 
                    object.topic_button['background'] = 'white'
                elif e.widget.cget('text') == 'Topics': 
                    object.topics_button['background'] = 'white'
                elif e.widget.cget('text') == 'Message': 
                    object.message_button['background'] = 'white'
                elif e.widget.cget('text') == 'Stream': 
                    object.stream_button['background'] = 'white'
                elif e.widget.cget('text') == 'Get': 
                    object.get_button['background'] = 'white'
                elif e.widget.cget('text') == 'Listen': 
                    object.listen_button['background'] = 'white'
                    
            
            # Bind button actions 
            def bind_buttons(object): 
                object.topic_button.bind("<Enter>", on_enter)
                object.topic_button.bind("<Leave>", on_leave)
                
                object.topics_button.bind("<Enter>", on_enter)
                object.topics_button.bind("<Leave>", on_leave)
                
                object.message_button.bind("<Enter>", on_enter)
                object.message_button.bind("<Leave>", on_leave)
                
                object.stream_button.bind("<Enter>", on_enter)
                object.stream_button.bind("<Leave>", on_leave)
                
                object.get_button.bind("<Enter>", on_enter)
                object.get_button.bind("<Leave>", on_leave)
            
                object.listen_button.bind("<Enter>", on_enter)
                object.listen_button.bind("<Leave>", on_leave)
                
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
                object.topic_button.grid(row=0, column=0)
                object.topics_button.grid(row=1, column=0)
                object.message_button.grid(row=2, column=0)
                object.stream_button.grid(row=3, column=0)
                object.get_button.grid(row=4, column=0)            
                object.listen_button.grid(row=5, column=0)
                object.test_button.grid(row=6, column=0)
                object.start_button.grid(row=7, column=0)
                object.stop_button.grid(row=8, column=0)
                object.close_button.grid(row=9, column=0)
                
                
            # Init elements 
            def init_elm(object):
                object.button_frame = Frame(object.root, borderwidth=2, border=1)
                object.button_frame.grid(row=1, column=0, pady=50, padx=(50,25))
                
                object.test_button = Button(object.button_frame, text="Test", command= lambda:test_seq(object), width=15, state='normal', bg = 'white')
                object.start_button = Button(object.button_frame, text="Start/Send", command= lambda:start_send_seq(object), width=15, state='disabled', bg = 'white')
                object.stop_button = Button(object.button_frame, text="Stop", command= lambda:stop_seq(object), width=15, state='disabled', bg = 'white')
                object.close_button = Button(object.button_frame, text="Close", command= lambda:close(object), width=15, state='normal', bg = 'white')
                
            init_elm(object)
            pack_buttons(object)            
            bind_buttons(object)
            
        
        init_button_frames(self)
        init_input_frames(self)
        
        
        self.title = Label(self.root, text=str(self.title_txt).upper()) 
        self.title.grid(row=10, columnspan=15)