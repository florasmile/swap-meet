from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id=None, width=0, length=0):
        super().__init__(id)
        self.width = width
        self.length = length
    
    def __str__(self):
        general_description = super().__str__()
        return " ".join([general_description, self.display_size_message()])
    
    def display_size_message(self):
        return f"It takes up a {self.width} by {self.length} sized space."
