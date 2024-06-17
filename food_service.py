from order import Order
from uuid import uuid4
from order_status import OrderStatus
class FoodService:
    instance=None 
    def getInstance():
        if FoodService.instance is None:
            FoodService.instance=FoodService()
        return FoodService.instance 
    
    def __init__(self):
        self.customer_list={}
        self.resturant_list={}
        self.delivery_agent={}
        self.orders_list={}
        self.order_items=[]
    def register_customer(self,customer):
        self.customer_list[customer.id]=customer 
        return self.customer_list
    def register_resturant(self,resturant):
        self.resturant_list[resturant.id]=resturant
        return self.resturant_list
    def register_delivery_agent(self, delivery_agent):
        self.delivery_agent[delivery_agent.id]=delivery_agent
        return self.delivery_agent
    
    def retrieve_available_resturant(self,id):
        resturant=self.resturant_list[id]
        if resturant is not None:
            return resturant 
    def retrieve_available_resturant_menue(self,id):
        resturant=self.resturant_list[id]
        if resturant is not None:
            return resturant.menue_items
    def get_all_order_items(self,order):
        self.order_items.append(order)
        return self.order_items
        
    def place_order(self,customer_id,resturant_id,order_items):
        customer=self.customer_list[customer_id]
        resturant=self.resturant_list[resturant_id]
        cost=0
        for order in order_items:
            cost+=order.get_price()
        
        if customer and resturant and order_items:
            id=str(uuid4())
            order=Order(id,customer,resturant,order_items,None,cost)
            self.orders_list[id]=order 
        return order.id
    def get_orders_from_orderid(self,id):
        if id in self.orders_list:
            return self.orders_list[id]
    def assign_delivery_partner(self,order):
        for agent in self.delivery_agent.values():
            if agent.availability_status==True:
                order.delivery_agent=agent
                agent.availability_status=False 
    def update_order_status(self,order_id,status):
        order=self.orders_list[order_id]
        if order is not None:
                order.status=status
                if order.status!=OrderStatus.CANCELLED:
                    self.assign_delivery_partner(order)
    def order_delivered(self,order):
        if order.status!=OrderStatus.CANCELLED and order.status==OrderStatus.INPROGRESS:
            order.status=OrderStatus.DELEIVERED 
        delivery_agent=order.delivery_agent 
        delivery_agent.availability_status=True
            
        