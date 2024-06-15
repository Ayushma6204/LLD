from split import Split
class ExactSplit(Split):
    def __init__(self,user,amount):
        super().__init__(user)
        self.amount=amount
    def getAmount(self):
        return self.amount