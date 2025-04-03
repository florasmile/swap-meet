from swap_meet.item import Item

class Vendor:
    """A class representing a vendor who wants to swap items with other vendors

    Attributes:
        inventory (list): a list of items to swap with other vendors.
    """

    def __init__(self, inventory = None):
        """Initializes the vendor with given inventory or set to None as default.

        Args:
            inventory(list): a list of items            
        """
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
        """Swaps items between the current vendor and another vendor.

        Parameters:
            other_vendor (Vendor): The vendor to swap items with.
            my_item (Item): The item the current vendor wants to trade.
            their_item (Item): The item the other vendor wants to trade.

        Returns:
            bool: True if the swap is successful, otherwise False.

        """
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.remove(my_item)
        other_vendor.remove(their_item)

        other_vendor.add(my_item)
        self.add(their_item)

        return True
    
    def swap_first_item(self, other_vendor):
        """Swaps the first item of the current vendor's inventory with the first item of the other vendor's inventory.

        Parameters:
            other_vendor (Vendor): The vendor to swap with.

        Returns:
            bool: True if the swap is successful, otherwise False.
        """
        if not self.inventory or not other_vendor.inventory:
            return False
        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]

        return self.swap_items(other_vendor, my_item, their_item)

    def get_by_category(self, category):
        """Returns a list of items in the inventory that belong to a specific category.

        Parameters:
            category (str): The category to filter items by.

        Returns:
            list: A list of items that match the given category.
        """
        # item_list = []
        # for item in self.inventory:
        #     if item.get_category() == category:
        #         item_list.append(item)
        # use list comprehension to simplify code
        return [item for item in self.inventory if item.get_category() == category]
    
    def get_best_by_category(self, category):
        """Returns the item with the best condition in a given      category.

        Parameters:
            category (str): The category to search for the best item.

        Returns:
            Item or None: The item with the best condition in the specified category, or None if no items match.
        """
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
        """Swaps the best items based on categories between vendors.

        Parameters:
            other_vendor (Vendor): The vendor to swap with.
            my_priority (str): The category the current vendor prioritizes.
            their_priority (str): The category the other vendor prioritizes.
        
        Returns:
            bool: True if the swap is successful, otherwise False.
        """
        my_best_item = self.get_best_by_category(their_priority)

        their_best_item = other_vendor.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False
        
        return self.swap_items(other_vendor, my_best_item, their_best_item)
    
    def swap_by_newest(self, other_vendor):
        """Swaps the newest item between two vendors.

        Parameters:
            other_vendor (Vendor): The vendor to swap with.

        Returns:
            bool: True if the swap is successful, otherwise False.
        """
        my_newest_item = self.get_newest_item()
        their_newest_item = other_vendor.get_newest_item()

        if not my_newest_item or not their_newest_item:
            return False
        
        return self.swap_items(other_vendor, my_newest_item, their_newest_item)

    # Helper Function
    def get_newest_item(self):
        """Returns the newest item (based on age) in the vendor's inventory.

        Returns:
            Item or None: The newest item, or None if the inventory is empty.
        """
        if not self.inventory:
            return None
        
        newest_item = self.inventory[0]
        min_age = newest_item.age

        for item in self.inventory: 
            if item.age < min_age:
                min_age = item.age
                newest_item = item

        return newest_item

