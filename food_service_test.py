import unittest
from unittest.mock import Mock, patch
from food_service import  FoodService
from customer import Customer 
from resturant import Resturant 
from menue_item import MenueItem 
from order_status import OrderStatus 
from order_item import OrderItem 
from delivery import Delivery 

class TestFoodService(unittest.TestCase):

    def setUp(self):
        self.food_service=FoodService.getInstance()
        self.customer=Customer(101, "Ayushma", "bahugunaayushma@gmail.com", 7088776204)
        self.menu_item = MenueItem(1, "White Sauce Pasta", "Zucchini White Sauce Alfredo Pasta", 250)
        self.restaurant = Resturant(201, "Cafe De Vine", "Dehradun", [self.menu_item])
        self.delivery_agent=Delivery(90,"Agent1",9456312740)
        

    def test_place_order(self):
        self.food_service.register_customer(self.customer)
        self.food_service.register_resturant(self.restaurant)
        self.food_service.register_delivery_agent(self.delivery_agent)
        
        
        self.food_service.place_order(self.customer.id, self.restaurant.id, self.order_item)
        

        

if __name__ == "__main__":
    unittest.main()

