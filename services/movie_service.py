from models.movie import Movie
from uuid import uuid4
class MovieService:
    def __init__(self):
        self.movie_list={}
    
    def create_movie(self,name):
        id=str(uuid4())
        movie=Movie(id,name)
        self.movie_list[id]=movie 
        # print(self.movie_list)
        return self.movie_list
    
    def get_list_of_movies(self):
        list_of_movies=[]
        for movie in self.movie_list.values():
            list_of_movies.append(movie)
        # print(list_of_movies)
        return list_of_movies
        
        