from threading import Lock
class Ingredients:
    def __init__(self,name,quantity):
        self.name=name 
        self.quantity=quantity
        self.lock=Lock()
    
    def update_quantity(self,new_quantity):
        with self.lock:
            self.quantity+=new_quantity
