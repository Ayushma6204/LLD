from split import Split
class PercentageExpense(Split):
    def __init__(self, user, percent):
        super().__init__(user)
        self.percent=percent