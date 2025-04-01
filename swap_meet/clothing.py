from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id = None, fabric = "Unknown"):
        super().__init__(id)
        self.fabric = fabric
    
    def __str__(self):
        general_description = super().__str__()
        return f"{general_description} It is made from {self.fabric} fabric."
    