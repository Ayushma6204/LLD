from services.theatre_service import TheatreService 
from services.movie_service import MovieService 
from services.screen_service import ScreenService 
from services.show_service import ShowService 
from services.booking_Service import BookingService
from services.seats_service import Seat_Service 
from models.user import User
def run():
    theatre_service = TheatreService()
    theatre_service.add_theatre("SilverCity")
    seats_service=Seat_Service()
    seats_service.generateSeats(100)
    screen_service=ScreenService()
    screen_service.add_screens("Screen1",theatre_service,seats_service)
    movie_service=MovieService()
    movie_service.create_movie("Avengers")
    show_service=ShowService()
    show_service.create_show(movie_service,"18:00",120,screen_service)
    booking_service=BookingService()
    user=User(101,"Ayushma","aayu@gmail.com")
    
    booking_service.create_booking(show_service,movie_service,user.id,seats_service)
    
    print(booking_service)
   
if __name__ == "__main__":
    run()