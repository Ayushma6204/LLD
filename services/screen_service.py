from uuid import uuid4
from models.screens import Screens
from services.seats_service import Seat_Service
class ScreenService:
    def __init__(self):
        self.screen_service={}
    def add_screens(self,name,theatre):
        seat_service=Seat_Service()
        seats=seat_service.generateSeats(100)
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
    