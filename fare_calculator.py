from abc import ABC,abstractclassmethod 

class FareCalculator(ABC):
    @abstractclassmethod
    def fare_calculator(self,ride):
        pass
        