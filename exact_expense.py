from expense import Expense
from split_type import SplitType
from exact_split import ExactSplit
class ExactExpense(Expense):
    def __init__(self, amount, paid_by, type, splits):
        super().__init__(amount,paid_by,type,splits)
    def validate(self):
        for split in self.splits:
            print(split)
            if not isinstance(split,ExactSplit):
                return False 
        amount=self.amount 
        sumAmount=0 
        for split in self.splits:
            exactSplit = split
            sumAmount += exactSplit.getAmount()
        if  amount!= sumAmount:
                return False
        return True
                            