"""
This is a meal class. It contains a list of food items.

November 19, 2021 
- Created class
"""

class meal:

    # Constructor for the class
    def __init__(self, name):
        # List of food items
        self.list_of_foods = []
        self.name = name

    # Adding food to the list. Returns -1 
    # if the item is in the list and 0 if it added 
    # and item successfully.
    def add_foods (self, new_food):
        
        # If the item is in the list.
        if (new_food in self.list_of_foods):
            return -1

        # Otherwise add to the list
        else:
            self.list_of_foods.append(new_food)
            return 0

    def change_name (self, new_name):
        self.name = new_name
    
    def get_name (self):
        return self.name
    
    # Returning a food item of the given name.
    # Returns a food item if found or None if none found.
    def find_food_item (self, food_name):
        
        # Loop through the list and find the item. 
        for x in self.list_of_foods:
            if (x.get_name == food_name):
                return x
        
        return None # No item found
        
    