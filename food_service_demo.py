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
    print(menue_items)
    resturant=Resturant(201,"Cafe De Vine","Dehradun",menue_items)
    food_service.register_resturant(resturant)
    order_items=OrderItem(menue_items,2)
    delivery_agent=Delivery(90,"Agent 1",94563128740)
    food_service.register_delivery_agent(delivery_agent)
    order=food_service.place_order(customer.id,resturant.id,order_items)
    food_service.update_order_status(order.id,OrderStatus.CONFIRMED)
    

if __name__ == "__main__":
    main()