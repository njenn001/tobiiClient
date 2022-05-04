import os 
import threading
import time 

#from user import User 
#from producer import Producer 

class Scenario(): 
    # Class init 
    def __init__(self, *args):
        
        # Native descriptors 
        self.os_name = ''
        self.style = '' 
        self.py_version = ''
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
                
        # Threads 
        self.t_list = [] 
        self.virt_thread = None 
        self.nat_thread = None 
        
        # You 
        self.you = None
        self.args = None 
        
        self.init() 
                
    # GET / SET os name 
    def get_os_name(self): 
        return self.os_name
    def set_os_name(self, os_name):
        self.os_name = os_name 
        
    # GET / SET style  
    def get_style(self): 
        return self.style
    def set_style(self, style):
        self.style = style 
        
    # GET / SET python version 
    def get_py_version(self): 
        return self.py_version
    def set_py_version(self, py_version):
        self.py_version = py_version
       
    # GET / SET root directory 
    def get_root_dir(self): 
        return self.root_dir
    def set_root_dir(self, root_dir):
        self.root_dir = root_dir
    
    # GET / SET / ADD thread list
    def get_t_list(self): 
        return self.t_list
    def set_t_list(self, t_list):
        self.t_list = t_list
    def add_thread(self, thread): 
        self.t_list.append(thread)
    
    # GET / SET virtual thread 
    def get_virt_thread(self): 
        return self.virt_thread
    def set_virt_thread(self, virt_thread):
        self.virt_thread = virt_thread
    
    # GET / SET natural thread
    def get_nat_thread(self): 
        return self.nat_thread
    def set_nat_thread(self, nat_thread): 
        self.nat_thread = nat_thread

    # GET / SET you 
    def get_you(self): 
        return self.you
    def set_you(self, you):
        self.you = you
        
    # GET / SET args 
    def get_args(self): 
        return self.args
    def set_args(self, args):
        self.args = args
         
    # Init Scenario
    def init(self): 
        self.os_eval()
        self.version_check()
        
        self.configure_threads()
        
    # Clean project directories 
    def clean_sequence(self):
        
        # Windows Version
        def windows_clean(object): 
            try:
                os.system(r'rmdir app\__pycache__ /S /Q && del app\*.pyc')
            except Exception as ex: 
                print(ex) 
        # Linux Verison
        def linux_clean(object): 
            try: 
                os.system(r'rm -rf app\__pycache__')
            except Exception as ex: 
                print(ex) 
            
        if self.get_style() == 'Windows': 
            windows_clean(self)
        else: 
            linux_clean(self)
         
    # Empty terminal contents 
    def clear_screen(self): 
        if self.os_name == 'nt': 
            os.system('cls')
        else: 
            os.system('clear')
    
    # Throw exception with suggested fix / fix error 
    def throw_exc(self, msg): 
        
        # Python version exception 
        if msg == 'version':
            
            self.clean_sequence() 
            self.clear_screen() 
            raise Exception("Must be using Python 3.8.") 
        
        # Requirement file exception 
        elif msg == 'req':
            
            self.clean_sequence() 
            self.clear_screen() 
            raise Exception("Requirements.txt must exist.")
        
        elif msg == 'env': 
            
            self.clean_sequence() 
            self.clear_screen() 
            raise Exception("Error creating virtual environment.")

        elif msg == 'nat': 
            
            self.clean_sequence() 
            self.clear_screen() 
            raise Exception("Error creating natural environment.")

    # Stop all running threads
    def stop_threads(self): 
        try: 
            if len(self.get_t_list()) > 0: 
                for t in self.get_t_list():
                    if t.is_alive(): 
                        pass
                    else: 
                        t.join() 
        except Exception as ex: 
            print(ex)
            self.stop_threads() 
    
    # Configure scenario threads
    def configure_threads(self): 

        self.set_virt_thread( threading.Thread(target=self.virtual_init, args=([]) ) )
        self.set_nat_thread( threading.Thread(target=self.natural_init, args=([]) ) )  

    # Init virtual environment 
    def virtual_init(self): 
        
        self.add_thread(self.get_virt_thread())

        if self.get_os_name() == 'nt':
            try:
                print('\nCreating virtual environment ...\n')
                os.system(r"virtualenv venv")
                time.sleep(5)
                
                print('\nInstall virtual requirments ...\n')
                os.system(r'.\venv\Scripts\pip.exe install -r .\app\requirements.txt')
                
            except Exception as ex: 
                self.throw_exc('env')
        else: 
            try: 
                print('\nCreating virtual environment ...\n') 
                os.system(r"virtualenv venv")
                time.sleep(5)
                    
                print('\nInstalling virtual requirments ...\n')
                os.system(r'./venv/bin/pip install -r ./app/requirements.txt')

            except Exception as ex: 
                self.throw_exc('env')

    # Init natural environment 
    def natural_init(self): 

        self.add_thread(self.get_nat_thread())
        
        if self.get_os_name() == 'nt': 
            try:        
                os.system(r'pip install -r app\requirements.txt')
            except Exception as ex:
                self.throw_exc('nat')
        else: 
            try:        
                os.system(r'pip install -r app/requirements.txt')
            except Exception as ex:
                self.throw_exc('nat')

    # Check version
    def os_eval(self): 
        self.set_os_name(os.name.replace(' ', '')) 
        
        if self.get_os_name() == 'nt': 
            self.set_style('Windows')
            print(self.get_style())
        else: 
            self.set_style('Linux')
            print(self.get_style())
        
    # Check Python version
    def version_check(self):  
        print('\nChecking Python Version ...')
        
        self.set_py_version(float( str(os.sys.version_info[0]) + "." + str(os.sys.version_info[1]) )) 
        if self.get_py_version() != 3.8:
            self.throw_exc('version')
        else: 
            print('\nCorrect Python version.')