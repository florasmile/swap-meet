from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, condition=0, age=0, fabric="Unknown"):
        super().__init__(id, condition, age)
        self.fabric = fabric
    
    def __str__(self):
        general_description = super().__str__()
        return " ".join([general_description, self.display_fabric_message()])
    
    def display_fabric_message(self):
        return f"It is made from {self.fabric} fabric."
    