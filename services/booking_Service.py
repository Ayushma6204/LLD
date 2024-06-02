from models.booking import Booking 
from uuid import uuid4
from threading import Lock
class BookingService:
    _instance=None
    def getInstance():
        if BookingService._instance is None:
            BookingService._instance=BookingService()
        return BookingService._instance 
    def __init__(self):
        self.booking_service={}
        self.lock=Lock()
    
    def create_booking(self,show,movie,user_id,seats):
        with self.lock():
            id=str(uuid4())
            booking=Booking(id,show,movie,user_id,seats)
            self.booking_service[id]=booking
            print(self.booking_service)
            return self.booking_service
        