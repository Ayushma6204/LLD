from enum import Enum 
class OrderStatus(Enum):
    PENDING=1 
    INPROGRESS=2 
    DELEIVERED=3 
    CANCELLED=4 
    CONFIRMED=5