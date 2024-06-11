class Group:
    def __init__(self,group_id,users_list):
        self.group_id=group_id 
        self.users_list=users_list
        self.expenses=[] 
    def add_expense(self,expense):
        self.expenses.append(expense)
        return self.expenses
        