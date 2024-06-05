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
    
    def get_list_of_screens(self,screens):
        print(screens)
        list_of_screens=[]
        for screen in screens:
            list_of_screens.append(screen)
        return list_of_screens        
        