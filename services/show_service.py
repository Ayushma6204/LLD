from models.shows import Shows
from uuid import uuid4
class ShowService:
    def __init__(self):
        self.show_service={}
    
    def create_show(self,movie,start_time,duration,screen):
        id=str(uuid4())
        show=Shows(id,movie,start_time,duration,screen)
        self.show_service[id]=show 
    def get_show(self,id):
        if id in self.show_service:
            return self.show_service[id]
        else:
            print("This show is not available")
    
    def get_show_for_screen(self,screen):
        show_response=[]
        for show in self.show_service:
            if show.screen==screen:
                show_response.append(show)
        print(show_response)
        return show_response
            
        