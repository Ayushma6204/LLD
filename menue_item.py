class MenueItem:
    def __init__(self,id,name,description,price):
        self.id=id
        self.name=name 
        self.descrption=description
        self.price=price
        self.availability=True
    def set_availability(self):
        self.availability=False