from models.shows import Shows
from uuid import uuid4
from models.show_seat import ShowSheat
class ShowService:
    def __init__(self):
        self.show_service={}
    
    def create_show(self,start_time,duration,screen):
        id=str(uuid4())
        seats=screen.seats
        total_seats=[]
        for seat in seats:
            s=ShowSheat(seat)
            total_seats.append(s)
        show=Shows(id,total_seats,start_time,duration,screen)
        self.show_service[id]=show 
    def get_show(self,id):
        if id in self.show_service:
            return self.show_service[id]
        else:
            print("This show is not available")
    
    def get_show_for_theatre(self,theatre):
        show_response=[]
        for show in self.show_service.values():
            if show.screen.theatre==theatre:
                show_response.append(show)
        # print(show_response)
        return show_response
            
        