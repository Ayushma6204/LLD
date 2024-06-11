from transaction import Transaction
from split_type import SplitType
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
    def addExpense(self,group_id,expense):
        group=self.group_list[group_id]
        if group :
            group.expense=expense 
    def validate_expense(self,expense,instance_):
        if expense.type==instance_:
            return True 
        return False
    
    def split_expense(self,expense):
        amount=expense.amount 
        total_splits = len(expense.splits)
        split_amount = amount / total_splits
        
        if expense.type==SplitType.PERCENT or expense.type==SplitType.EXACT:
            
            if expense.type==SplitType.PERCENT:
                if self.validate_expense(expense,SplitType.PERCENT):
                    for split in expense.splits:
                        person=split.user 
                        if person!=expense.paid_by:
                            percent=split.percent
                            amount_=round((amount*percent)/100,2) 
                            person.update_balances(person,amount_,expense.paid_by)
            
                else:
                    print("Invalidate Expense")
            else:
                if self.validate_expense(expense,SplitType.EXACT):
                    for split in expense.splits:
                        person=split.user 
                        if person!=expense.paid_by:
                            amount_=split.amount
                            person.update_balances(person,amount_,expense.paid_by)
                           
                else:
                    print("Invalidate Expense")
        else:
            for split in expense.splits:
                person=split.user 
                if person!=expense.paid_by:
                    person.update_balances(split.user,split_amount,expense.paid_by)
                
                
                   
                
                
            
 
            
            
    def createTransaction(self,amount,sender,receiver):
        id=SplitWise.generate_transaction_id()
        trsaction=Transaction(id,amount,sender,receiver)
    