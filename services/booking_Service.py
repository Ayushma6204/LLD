from models.booking import Booking 
from uuid import uuid4
from models.seat_type import Seat_Type
from models.seat_status import Seat_status
from services.theatre_service import TheatreService
from services.seats_service import Seat_Service
from threading import Lock
from models.user_session import UserSession
import time
import threading
class BookingService:
    _instance=None
    def getInstance():
        if BookingService._instance is None:
            BookingService._instance=BookingService()
        return BookingService._instance 
    def __init__(self):
        self.booking_service={}
        self.lock=Lock()
    
    def create_booking(self,show,user_id,seat_num):
        all_seats=[]
        available_seats=show.available_seats
        for a in available_seats:
            if a.seat_status==Seat_status.AVAILABLE:
                all_seats.append(a.seat)
        print(f"Ayu{all_seats}")
        confirmed_seats=[]
        with self.lock:
            for seat in all_seats:
                if int(seat.number[1:]) in seat_num:
                    confirmed_seats.append(seat)
                elif len(confirmed_seats)==len(seat_num):
                    break
                else:
                    print("next one!!")     
                
        id=str(uuid4())
        booking=Booking(id,show,user_id,confirmed_seats)
        self.booking_service[id]=booking
        print(self.booking_service)
        return self.booking_service
    
    def get_all_bookings(self):
        list_of_booking=[]
        for booking in self.booking_service.values():
            list_of_booking.append(booking) 
        return list_of_booking
    def reserve_seat(self,user_id,show,future_requested_seats):
        session_obj=UserSession(user_id,60)
        threading.Timer(2, self.cancel_reservation, [user_id,show,future_requested_seats]).start()
        available_seats=show.available_seats
        reserve={}
        reserve[user_id]=[]
        for a in available_seats:
            if a.seat_status==Seat_status.AVAILABLE and int(a.seat.number[1:]) in future_requested_seats:
                a.seat_status=Seat_status.RESERVED
                reserve[user_id].append(a.seat)
            else:
                print("Seat is already occupied")
    def cancel_reservation(self,user_id,show,future_requested_seats):
        print("Canceled")
            
        
    def make_payment(self,user_id):
        session_obj=UserSession(user_id,60)
        if not session_obj.is_expired():
            
            print("Processing  Payment")
            print("Payment SUCCESSFUL.")
        else:
                print("Payment FAILED. Retrying payment...")
                time.sleep(1)
            
            
            
        
       
    
        