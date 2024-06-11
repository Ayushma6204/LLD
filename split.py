from abc import ABC, abstractmethod
class Split(ABC):
    def __init__(self, user):
        self.user = user
       
     
    
# #     @abstractmethod
# #     def set_amount(self):
# #         pass
# class Split:
#     def __init__(self,user,amount):
#         self.user=user 
#         self.amount=amount