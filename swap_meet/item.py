import uuid
class Item:
    def __init__(self, id = None):
        self.id = uuid.uuid4().int if id is None else id
    
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."