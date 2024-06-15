from split import Split
class PercentageSplit(Split):
    def __init__(self, user, percent):
        super().__init__(user)
        self.percent=percent
        