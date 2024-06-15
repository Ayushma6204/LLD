from transaction import Transaction
from split_type import SplitType
from exact_expense import ExactExpense
from percent_expense import PercentageExpense
class SplitWise:
    _instance=None 
    TRANSACTION_ID_PREFIX = "TXN_"
    transaction_counter = 0
    @classmethod
    def generate_transaction_id(cls):
        cls.transaction_counter += 1
        transaction_number = cls.transaction_counter
        return cls.TRANSACTION_ID_PREFIX + f"{transaction_number:06d}"
    @staticmethod
    def getInstance():
        if SplitWise._instance is None:
            SplitWise._instance=SplitWise()
        return SplitWise._instance 
    
    def __init__(self):
        self.user_list={}
        self.group_list={}
       

        
    def addUser(self,user):
        self.user_list[user.id]=user 
        return self.user_list
    def add_group(self,group):
        self.group_list[group.id]=group
        return self.group_list
    def addExpense(self,group,expense):
        if group :
            group.expense=expense 
            # self.split_expense(expense)
                
                   
    def settle_balance(self,user1,user2):
        user2_owns=0
        user1_owns=0
        if user1.name in user2.balances:
            user1_owns=user2.balances[user1.name]
        if user2.name in user1.balances:
            user2_owns=user1.balances[user2.name]
        balance=user1_owns-user2_owns
        if balance<0:
            self.createTransaction(user1,user2,balance)
            user1.balances[user2.name]=0.0 
        elif balance>0:
            self.createTransaction(user2,user1,balance)
            user2.balances[user1.name]=0.0 
        else:
            print("No due left")
      
                                
                
    def create_expense(self,amount,paid_by,type,splits):
        if type == SplitType.EXACT:
            exact_expense=ExactExpense(amount, paid_by, type,splits)
            if exact_expense.validate():
                for split in splits:
                    amount=split.amount 
                    user=split.user 
                    if user!=paid_by:
                        paid_by.update_balances(user,amount)
                print(paid_by.balances)
        elif type == SplitType.PERCENT:
            percent_expense=PercentageExpense(amount, paid_by, type,splits)
            if percent_expense.validate():
                for split in splits:
                    percent=split.percent 
                    user=split.user 
                    if user!=paid_by:
                        amount_to_given=round((amount*percent)/100,2)
                        paid_by.update_balances(user,amount_to_given)
                print(paid_by.balances)
            
            
    def createTransaction(self,receiver,sender,amount):
        id=SplitWise.generate_transaction_id()
        transaction=Transaction(id,amount,sender,receiver)
        return transaction
    