class Gaze(): 
    def __init__(self): 
    
        self.l_x = 0 
        self.l_y = 0 
        self.r_x = 0 
        self.r_y = 0 
        self.l_mm = 0 
        self.r_mm = 0

        self.l_position = []
        self.r_position = []
        self.gaze_position = []

    # GET / SET l_x
    def get_l_x(self): 
        return self.l_x
    def set_l_x(self, l_x): 
        self.l_x = l_x
    
    # GET / SET l_y
    def get_l_y(self): 
        return l_y
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
    
    # GET / SET l_position
    def get_l_position(self): 
        return self.l_position
    def set_l_position(self, l_position): 
        self.l_position = l_position
    
    # GET / SET r_position
    def get_r_position(self): 
        return self.r_position
    def set_r_position(self, r_position): 
        self.r_position = r_position
    
    # GET / SET gaze_position
    def get_gaze_position(self): 
        return self.gaze_position
    def set_gaze_position(self, gaze_position):
        self.gaze_position = gaze_position








