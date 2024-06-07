from machine import Machine
from payment import Payment
def run():
    m=Machine.getInstance()
    menue=m.intialisemenue()
    print(menue)
    ingredients=m.initialiseIngredients()
    coffee=m.select_coffee("latte")
    coffee_1=m.select_coffee("latte")
    
    payment=Payment(500)
    m.despense_coffee(coffee,payment)
    m.despense_coffee(coffee_1,payment)
    m.despense_coffee(coffee_1,payment)
    m.despense_coffee(coffee_1,payment)
   
    
if __name__ == "__main__":
    run()