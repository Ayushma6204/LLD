from food_service import FoodService 
from menue_item import MenueItem 
from order_item import OrderItem 
from order_status import OrderStatus 
from resturant import Resturant 
from customer import Customer
from delivery import Delivery
def main():
    food_service=FoodService.getInstance()
    customer=Customer(101,"Ayushma","bahugunaayushma@gmail.com",7088776204)
    food_service.register_customer(customer)
    menue_items=MenueItem(1,"Whit Sauce Pasta","Zukkini White Sauce Alfreddo Pasta",250)
    resturant=Resturant(201,"Cafe De Vine","Dehradun",menue_items)
    food_service.register_resturant(resturant)
    
    order_item=OrderItem(menue_items,2)
    order_items=food_service.get_all_order_items(order_item)
    delivery_agent=Delivery(90,"Agent 1",94563128740)
    food_service.register_delivery_agent(delivery_agent)
    order_id=food_service.place_order(customer.id,resturant.id,order_items)
    food_service.update_order_status(order_id,OrderStatus.CONFIRMED)
    

if __name__ == "__main__":
    main()