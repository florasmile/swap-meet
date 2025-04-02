from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        
        self.inventory.remove(item)
        return item
    
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.remove(my_item)
        other_vendor.remove(their_item)

        other_vendor.add(my_item)
        self.add(their_item)

        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        #self.inventory.pop(0)

        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]

        return self.swap_items(other_vendor, my_item, their_item)

    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            if item.get_category() == category:
                item_list.append(item)
        return item_list
    
    def get_best_by_category(self, category):
        # get items with matching category
        item_list = self.get_by_category(category)
        if not item_list:
            return None
        best_condition = item_list[0].condition
        best_item = item_list[0]
        for item in item_list:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)

        their_best_item = other_vendor.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False
        
        return self.swap_items(other_vendor, my_best_item, their_best_item)
    
    def swap_by_newest(self, other_vendor):
        my_newest_item = self.get_newest_item()
        their_newest_item = other_vendor.get_newest_item()

        if not my_newest_item or not their_newest_item:
            return False
        
        return self.swap_items(other_vendor, my_newest_item, their_newest_item)

    # Helper Function
    def get_newest_item(self):
        if not self.inventory:
            return None
        
        newest_item = self.inventory[0]
        min_age = newest_item.age

        for item in self.inventory: 
            if item.age < min_age:
                min_age = item.age
                newest_item = item

        return newest_item

