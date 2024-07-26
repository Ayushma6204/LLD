from fare_calculator import FareCalculator 
import math
class DistanceFareCalculator(FareCalculator):
    def __init__(self,rate):
        self.rate=rate 
    
    def calculate_distance(self,ride):
        pickup_point=ride.pickup_loc 
        drop_point=ride.drop_loc 
        distance=0
        for x,u in zip(pickup_point,drop_point):
            distance = math.sqrt(sum((p - d) ** 2 for p, d in zip(pickup_point, drop_point)))
        return distance
            
    def fare_calculator(self,ride):
        distance=self.calculate_distance(ride)
        return distance*self.rate