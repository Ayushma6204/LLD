from expense import Expense
from split_type import SplitType
from percentage_split import PercentageSplit
class PercentageExpense(Expense):
    def __init__(self, amount, paid_by, type, splits):
        super().__init__(amount,paid_by,type,splits)
    def validate(self):
        for split in self.splits:
            print(split.__dict__)
            if not isinstance(split,PercentageSplit):
                return False 
        sumofpercent=0 
        for split in self.splits:
            sumofpercent += split.percent
        if  100!= sumofpercent:
                return False
        return True
                            