from uuid import uuid4
from models.screens import Screens
class ScreenService:
    def __init__(self):
        self.screen_service={}
    def add_screens(self,name,theatre,seats):
        id=str(uuid4())
        screen=Screens(id,name,theatre,seats)
        self.screen_service[id]=screen
        print(self.screen_service)
        return self.screen_service 
    
    def get_screen_for_theatre(self,theatre):
        screen_list=[]
        for screen in self.screen_service.values():
            if screen.theatre==theatre:
                screen_list.append(screen)
        print(screen_list)
        return screen_list