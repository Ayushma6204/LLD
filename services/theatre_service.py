from uuid import uuid4
from models.theatre import Theatre
class TheatreService:
    def __init__(self):
        self.theatre_list={}
    
    def add_theatre(self,name):
        id=str(uuid4())
        theatre=Theatre(id,name)
        self.theatre_list[id]=theatre
        print(self.theatre_list) 
        return self.theatre_list
        
        