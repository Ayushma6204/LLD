from fare_calculator import FareCalculator 
import math
class TimeFareCalculator(FareCalculator):
    def __init__(self,rate):
        self.rate=rate 
    
    def calculate_time(self,ride):
        pickup_point=ride.pickup_loc 
        drop_point=ride.drop_loc 
        time=0
        for x,u in zip(pickup_point,drop_point):
            time=len(pickup_point)
            
        return time
            
    def fare_calculator(self,ride):
        time=self.calculate_distance(ride)
        return time*self.rate