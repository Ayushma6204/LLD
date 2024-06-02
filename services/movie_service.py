from models.movie import Movie
from uuid import uuid4
class MovieService:
    def __init__(self):
        self.movie_list={}
    
    def create_movie(self,name):
        id=str(uuid4())
        movie=Movie(id,name)
        self.movie_list[id]=movie 
        print(self.movie_list)
        return self.movie_list
        
        