import uuid
class Item:
    def __init__(self, id = None, condition=0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition
    
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        condition_scale = {
            0:"Broken / Junk",
            1:"Heavily Used",
            2:"Used - Fair",
            3:"Used - Good",
            4:"Like New",
            5:"Brand New"
        }
        return condition_scale[self.condition]