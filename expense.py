from abc import ABC, abstractmethod

class Expense(ABC):
    def __init__(self, amount, paid_by, type, splits):
        self.amount = amount
        self.paid_by = paid_by
        self.type=type
        self.splits = splits
      

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def get_paid_by(self):
        return self.paid_by

    def set_paid_by(self, paid_by):
        self.paid_by = paid_by

    def get_splits(self):
        return self.splits

    def set_splits(self, splits):
        self.splits = splits

    def get_meta_data(self):
        return self.meta_data

    def set_meta_data(self, meta_data):
        self.meta_data = meta_data

    # @abstractmethod
    # def validate(self):
    #     pass
