from models.seats import Seats 
from models.seat_status import Seat_status 
from models.seat_type import Seat_Type
class Seat_Service:
    def __init__(self):
        self._seats=[]
    def generateSeats(self,no_of_seats):
        for i in range(1, no_of_seats + 1):
            seat_number = "S" +str(i)
            seat_type = Seat_Type.PLATINIUM if i <= 10 else Seat_Type.GOLD if i <= 30 else Seat_Type.SILVER
            self._seats.append(Seats(seat_number, seat_type))
        return self._seats
    # def selectSeats(self,no_of_seats):
    #     requested_seats=[]
    #     for seat in self.available_seats:
            
    #         if no_of_seats>0 and seat.seat_status==Seat_status.AVAILABLE:
    #             requested_seats.append(seat)
    #             seat.seat_status=Seat_status.BOOKED 
    #             no_of_seats-=1
    
    #     print(requested_seats)
    #     return requested_seats
    
    # def get_list_of_seats(self):
    #     available_seats=[]
    #     print(f"SSS{self._seats}")
    #     for seat in self._seats:
    #         print(f"SSS{seat}")
    #         if seat.seat_status==Seat_status.AVAILABLE:
    #             available_seats.append(seat)
    #     # print(f"Chutiya{available_seats}")
    #     return available_seats
        
    