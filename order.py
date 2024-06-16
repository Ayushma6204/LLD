from order_status import OrderStatus
class Order:
    def __init__(self,id,customer,resturant,order_item,delivery_agent):
        self.id=id 
        self.customer=customer 
        self.resturant=resturant 
        self.order_item=order_item 
        self.delivery_agent=delivery_agent
        self.status=OrderStatus.PENDING
        