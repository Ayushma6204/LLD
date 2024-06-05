from models.seats import Seats
from models.seat_status import Seat_status
class ShowSheat:
    def __init__(self,seat):
        self.seat_status=Seat_status.AVAILABLE 
        self.seat=seat
        