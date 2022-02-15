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
        self.inst_thread = None 
        
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
    
    # GET / SET install thread 
    def get_inst_thread(self): 
        return self.inst_thread
    def set_inst_thread(self, inst_thread):
        self.inst_thread = inst_thread
    
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
        
        self.set_inst_thread( threading.Thread(target=self.virtual_init, args=([]) ) )
        self.add_thread(self.get_inst_thread())
        #self.inst_thread.start() 
        
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
            
            
            
            raise Exception("Must be using Python 3.8.") 
        
        # Requirement file exception 
        elif msg == 'req':
            
            

            raise Exception("Requirements.txt must exist.")
        
        elif msg == 'Env': 
            
            
            
            raise Exception("Windows virtual environment.")

        elif msg == 'env': 
            
            
            
            raise Exception("Linux virtual environment.")

    # Stop all running threads
    def stop_threads(self): 
        try: 
            for t in self.get_t_list():
                if not t.is_alive(): 
                    t.join() 
        except Exception as ex: 
            self.stop_threads() 
    
    # Init virtual environment 
    def virtual_init(self): 
        if self.get_os_name() == 'nt':
            try:
                print('\nCreating virtual environment ...\n')
                os.system("virtualenv " + self.get_root_dir()  + r"\..\venv")
                time.sleep(5)
                
                os.sys.execuatble = str(self.get_root_dir() + r"\venv\Scripts\python.exe")
                val = os.system(r'.\venv\Scripts\activate.bat')
                if val == 0: 
                    
                    print('\nActivating virtual environment ...\n')
                    os.system(r'.\venv\Scripts\activate.bat')
                    
                    print('\nInstall virtual requirments ...\n')
                    os.system(r'.\venv\Scripts\pip.exe install -r .\app\requirements.txt')
            except Exception as ex: 
                self.throw_exc('Env')
        else: 
            try: 
                print('\nCreating virtual environment ...\n') 
                os.system("virtualenv " + self.get_root_dir() + r"/../venv")
                time.sleep(5)
                
                os.sys.execuatble = self.get_root_dir() + r"/venv/bin/python"
                val = os.system(r'./venv/bin/activate')
                if val == 0: 
                    
                    print('\nActivating virtual environment ...\n')
                    os.system(r'./venv/bin/activate')
                    
                    print('\nInstalling virtual requirments ...\n')
                    os.system(r'./venv/bin/pip install -r ./app/requirements.txt')
            except Exception as ex: 
                self.throw_exc('env')
                 
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