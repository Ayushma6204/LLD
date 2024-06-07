from coffee import Coffee
from ingredients import Ingredients
class Machine:
    _instance=None
    @staticmethod
    def getInstance():
        if Machine._instance is None:
            Machine._instance=Machine()
        return Machine._instance
    def __init__(self):
        self.menue=[]
        self.ingredients={} 
    def intialisemenue(self):
        espresso_recipe = {
            "coffee": 10,
            "water": 10
        }
        coffee=Coffee("expresso",200,espresso_recipe)
        self.menue.append(coffee)
        cappuccinoRecipe= {
            "coffee":10,
            "water":10,
            "milk":10
        }
        coffee=Coffee("cappuccino",250,cappuccinoRecipe)
        self.menue.append(coffee)
        latte_recipe={
            "coffee":5, 
            "milk":5,
            "water":5
        }
        
        coffee=Coffee("latte",230,latte_recipe)
        self.menue.append(coffee)
        return self.menue
       
        
    def initialiseIngredients(self):
        self.ingredients["coffee"]=Ingredients("Coffee",20) 
        
        self.ingredients["water"]=Ingredients("Water",20) 
        self.ingredients["milk"]=Ingredients("Milk",20) 
        return self.ingredients
    def display(self):
        for coffe in self.menue:
            print(f"{coffe.name} and price is {coffe.price}")
                            
    def select_coffee(self,order_coffee):
        for coffe in self.menue:
            if coffe.name==order_coffee:
                return coffe 

                             
    def update_ingradient(self,coffee):
        recipe=coffee.recipe 
        for ingredient,quantity in recipe.items():
            self.ingredients[ingredient].update_quantity(quantity)
    
    def hasEnoughIngredient(self,coffee):
        recipe=coffee.recipe 
        count=0
        for ingredient,quantity in recipe.items():
            print(ingredient,quantity)
            self.ingredients[ingredient].update_quantity(-quantity)
            m=self.ingredients[ingredient]
            if m.quantity<=3:
                count+=1
                print(f"{ingredient} running low")
        if count!=0:
            return False        
        return True
                
    def despense_coffee(self,coffee,payment):
        if coffee.price>payment.amount:
            print("Insufficient a mount")
        else:
            if self.hasEnoughIngredient(coffee):
                    print(coffee.recipe)
                    print(f"Dispensing {coffee.name}")
                    if payment.amount>coffee.price:
                        cash=payment.amount-coffee.price 
                        print(f"Please collect you {cash}")
            else:
                print(f"Shortage of ingrdients to make {coffee.name}")
        
            
        
        
        
          
                            
        