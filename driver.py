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
    screen_service=ScreenService()
    screen_service.add_screens("Screen1",theatre_service)
    screen_service.add_screens("Screen2",theatre_service)
    screen_service.add_screens("Screen2",theatre_service)
    movie_service=MovieService()
    movie_service.create_movie("Avengers")
    screen=screen_service.get_screen_for_theatre(theatre_service)
    show_service=ShowService()
    show_service.create_show("18:00",120,screen[0])
    show_service.create_show("21:00",120,screen[0])
    show=show_service.get_show_for_theatre(theatre_service)
    booking_service=BookingService()
    user=User(101,"Ayushma","aayu@gmail.com")
    
    x1=booking_service.create_booking(show[0],user.id,[1,50,99])
    x2=booking_service.create_booking(show[0],user.id,[1,50,99])
    ans=booking_service.get_all_bookings()
    m=booking_service.reserve_seat(user.id,show[0],[3,4,5])
    booking_service.make_payment(user.id)
    
    # print(ans[0].__dict__)
    
   
   
if __name__ == "__main__":
    run()