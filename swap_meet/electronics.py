from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, condition=0, age=None, type="Unknown"):
        super().__init__(id, condition, age)
        self.type = type
    
    def __str__(self):
        general_description = super().__str__()
        return " ".join([general_description, self.display_type_message()])
    
    def display_type_message(self):
        return f"This is a {self.type} device."
