"""
FoodItem class that is used to contain all of the information that a search food includes.

November 19, 2021
- Creation of class.


"""

# Class definition 
class FoodItem:

    # Constructor for the class.
    def __init__(self, name, calories):
        self.name = name # Name of the object
        self.calories = calories
        self.dictonary = {} # Create an empty dictionary 
    
    def get_name (self):
        return self.name
    
    def get_calories (self):
        return self.calories
    
    def get_dictonary (self):
        return self.dictonary

    # Might not need this one 
    def change_name(self, new_name):
        self.name = new_name
     
    def change_calories (self, new_calorie):
        self.calories = new_calorie
    
    # Method to add items to the dictionary. It returns -1 if there is an error 
    # or it returns 0 if it is able to add an item.
    def add_item (self, new_item, new_item_value):
        
        # If the value is in the dictionary already
        if (new_item in self.dictonary):
            return -1

        # We can add the item and its value
        else:
            self.dictionary [new_item] = new_item_value
            return 0
        








