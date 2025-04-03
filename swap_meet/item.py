import uuid
class Item:
    def __init__(self, id=None, condition=0, age=0):
        # original version before error handling
        # self.id = uuid.uuid4().int if id is None else id

        # generate unique id if id is not provided or not an integer
        self.id = uuid.uuid4().int if not isinstance(id, int) else id

        # error handling practice
        # try:
        #     if not id: 
        #         self.id = uuid.uuid4().int
        #     # raise error if id is not integer
        #     elif not isinstance(id, int):
        #         raise TypeError("id must be an integer")
        #     # if id is an integer passed during instantiation
        #     else:
        #         self.id = id
        # except TypeError as err:
        #     self.id = uuid.uuid4().int
        
        self.condition = condition
        self.age = age
    
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