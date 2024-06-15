from collections import defaultdict
class User:
    def __init__(self,id,name,email,password):
        self.id=id 
        self.name=name
        self.email=email 
        self.password=password 
        self.balances={}
    
    def update_balances(self,user,amount):
        self.balances[user.name] = amount

     
        return self.balances