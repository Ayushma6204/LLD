from menue_item import MenueItem 
class OrderItem:
    def __init__(self,menue_item,quantity):
        self.menue_item=menue_item 
        self.quantity=quantity 
    def get_price(self):
        price=self.menue_item.price 
        total_cost=price*self.quantity 
        return total_cost
    
        