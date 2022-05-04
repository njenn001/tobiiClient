import json

from matplotlib.font_manager import json_dump

class Gaze(): 
    def __init__(self, user): 
        
        self.user = user 
        
        self.l_x = 0 
        self.l_y = 0 
        self.r_x = 0 
        self.r_y = 0 
        self.l_mm = 0 
        self.r_mm = 0

        self.dict_ver = None
        self.json_ver = None 


    # GET / SET user 
    def get_user(self): 
        return self.user 
    def set_user(self, user): 
        self.user = user 

    # GET / SET l_x
    def get_l_x(self): 
        return self.l_x
    def set_l_x(self, l_x): 
        self.l_x = l_x
    
    # GET / SET l_y
    def get_l_y(self): 
        return self.l_y
    def set_l_y(self, l_y): 
        self.l_y = l_y 
    
    # GET / SET r_x
    def get_r_x(self): 
        return self.r_x
    def set_r_x(self, r_x): 
        self.r_x = r_x 
    
    # GET / SET r_y
    def get_r_y(self): 
        return self.r_y 
    def set_r_y(self, r_y): 
        self.r_y = r_y 
    
    # GET / SET l_mm
    def get_l_mm(self): 
        return self.l_mm
    def set_l_mm(self, l_mm): 
        self.l_mm = l_mm
    
    # GET / SET r_mm
    def get_r_mm(self):
        return self.r_mm
    def set_r_mm(self, r_mm):
        self.r_mm = r_mm

    # GET / SET dict version 
    def get_dict_ver(self): 
        return self.dict_ver
    def set_dict_ver(self, dict_ver): 
        self.dict_ver = dict_ver  

    # Export as string 
    def export(self): 
        out = "left_x" + str(self.get_l_x()) 
        +  " left_y" + str(self.get_l_y()) 
        + " right_x" + str(self.get_r_x()) 
        + " right_y" +  str(self.get_r_y()) 
        + " left_mm" + str(self.get_l_mm()) 
        + " right_mm" + str(self.get_r_mm())
    
        return out

    # Export as arrary 
    def export_dictionary(self): 

        o = {
            "left_x" : str(self.get_l_x()),
            "left_y" : str(self.get_l_y()),
            "right_x" : str(self.get_r_x()),
            "right_y" : str(self.get_r_y()),
            "left_mm" : str(self.get_l_mm()),
            "right_mm" : str(self.get_r_mm())
        }
        print(o)
        self.set_dict_ver(o) 
        return o

    # Export as JSON object
    def export_json(self): 
        o = json.dumps({
            "left_x" : str(self.get_l_x()),
            "left_y" : str(self.get_l_y()),
            "right_x" : str(self.get_r_x()),
            "right_y" : str(self.get_r_y()),
            "left_mm" : str(self.get_l_mm()),
            "right_mm" : str(self.get_r_mm())
        }, indent=4, default=str)

        return o 

        
    



