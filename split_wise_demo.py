from user import User 
from expense import Expense 
from split_type import SplitType 
from split_wise import SplitWise
from groups import Group
from split import Split
from exact_split import ExactSplit
from percentage_split import PercentageSplit
from split_type import SplitType
from exact_split import ExactSplit

def run():
    user_1=User(101,"Ayushma","bahugunaayushma@gmail.com","Welcome2cp")
    user_2=User(102,"Aayu","aayu@gmail.com","Superb!!")
    user_3=User(103,"Amisha","amisha@gmail.com","Zombie")
    split_wise=SplitWise.getInstance()
    split_wise.addUser(user_1)
    split_wise.addUser(user_2)
    users=split_wise.addUser(user_3)
    # split_1=ExactSplit(user_1,100)
    # split_2=ExactSplit(user_2,200)
    # split_3=ExactSplit(user_3,600)
    # expense=Expense(100,user_1,SplitType.EXACT,[split_1,split_2,split_3])
    split_10=ExactSplit(user_1,200)
    split_20=ExactSplit(user_2,150)
    split_30=ExactSplit(user_3,150)
    
    per_split10=PercentageSplit(user_1,30)
    per_split20=PercentageSplit(user_2,40)
    per_split30=PercentageSplit(user_3,30)
    # expense1=Expense(200,user_1,SplitType.PERCENT,[split_10,split_20,split_30])
    group=Group(201,users)
    expense=split_wise.create_expense(500,user_1,SplitType.PERCENT,[per_split10,per_split20,per_split30])
    split_wise.addExpense(group,expense)
    split_wise.settle_balance(user_1,user_2)
   
    
    
    
    


if __name__=='__main__':
    run()