from typing import Any


class Ride:
    def __init__(self):
        self.passengers_list=[]
        self.pickup_loc=[]
        self.drop_loc=[]
        self.total_fare=0
    
    def set_total_fare(self,total_fare):
        self.total_fare=total_fare
        return total_fare
    def add_passengers(self,passenger):
        self.passengers_list.append(passenger)
    
    def set_fare_for_passenger(self):
        if self.total_fare is None:
            raise Exception("Total fare is not set")
        for passenger in self.passengers_list:
            passenger.fare=self.total_fare//len(self.passengers_list)
    
    