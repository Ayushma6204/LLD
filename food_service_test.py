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
        self.order_items=OrderItem(self.menu_item,0)
        self.food_service.register_customer(self.customer)
        self.food_service.register_resturant(self.restaurant)
        self.food_service.register_delivery_agent(self.delivery_agent)

        
        

    def test_check_order_price(self):
        items_to_ordered=2 
        self.order_items.quantity=items_to_ordered 
        order_items=self.food_service.get_all_order_items(self.order_items)
        order_id=self.food_service.place_order(self.customer.id, self.restaurant.id,order_items)
        order=self.food_service.get_orders_from_orderid(order_id)
        self.assertEqual(order.price,500)
    def test_check_order_price_notequal(self):
        items_to_ordered=1
        self.order_items.quantity=items_to_ordered 
        order_items=self.food_service.get_all_order_items(self.order_items)
        order_id=self.food_service.place_order(self.customer.id, self.restaurant.id,order_items)
        order=self.food_service.get_orders_from_orderid(order_id)
        self.assertNotEqual(order.price,500)
    def test_order_delivered(self):
        order_items=self.food_service.get_all_order_items(self.order_items)
        order_id=self.food_service.place_order(self.customer.id, self.restaurant.id,order_items)
        order=self.food_service.get_orders_from_orderid(order_id)
        self.food_service.update_order_status(order_id,OrderStatus.INPROGRESS)
        self.food_service.order_delivered(order)
        self.assertEqual(order.status,OrderStatus.DELEIVERED)
    def test_order_cancelled(self):
        order_items=self.food_service.get_all_order_items(self.order_items)
        order_id=self.food_service.place_order(self.customer.id, self.restaurant.id,order_items)
        order=self.food_service.get_orders_from_orderid(order_id)
        self.food_service.update_order_status(order_id,OrderStatus.CANCELLED)
        self.assertEqual(order.status,OrderStatus.CANCELLED)
        
        

        

if __name__ == "__main__":
    unittest.main()

