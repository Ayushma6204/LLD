from collections import defaultdict
class User:
    def __init__(self,id,name,email,password):
        self.id=id 
        self.name=name
        self.email=email 
        self.password=password 
        self.balances=defaultdict(float)
    
    def update_balances(self,user,amount_,paid_by):
        self.balances[f"{user.name} owns {paid_by.name}" ] = amount_
     
        print(self.balances)
        return self.balances