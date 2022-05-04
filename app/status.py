class Status(): 
    def __init__(self): 

        self.connection_status = False 
        self.broker_str = ''
        self.port_str = '' 


    # GET / SET connection status
    def get_connection_status(self): 
        return self.connection_status
    def set_connection_status(self, connection_status): 
        self.connection_status = connection_status

    # GET / SET broker string 
    def get_broker_str(self): 
        return self.broker_str
    def set_broker_str(self, broker_str): 
        self.broker_str = broker_str
    
    # GET / SET port string 
    def get_port_string(self): 
        return self.port_str
    def set_port_string(self, port_str): 
        self.port_str = port_str