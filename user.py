class User:
    def __init__(self,id,name,email,password,reputation):
        self.id=id 
        self.name=name 
        self.email=email 
        self.password=password
        self.is_logged=False 
        self.reputation=reputation
    
    def log_in(self):
        print("Ayushma")
        self.is_logged=True
        return
    
    def log_out(self):
        self.is_logged=False