"""
FoodItem class that is used to contain all of the information that a search food includes.

November 19, 2021
- Creation of class.


"""

from API import API
NAME = 'item_name'
BRAND = 'brand_name'
CALORIES = 'nf_calories'
# Class definition 
class FoodItem:
    api = API()

    # Constructor for the class.

    def __init__(self, name):
        self.food_list = self.api.call_api(name)  # Name of the object
        self.name = ''
        self.brand = ''
        self.calories = ''
        self.dictionary = {}
        self.food_choice = self.food_list[0]

    def return_entire_foods_list(self):
        return self.food_list

    def get_name (self):
        return self.name

    def get_brand (self):
        return self.brand
    
    def get_calories (self):
        return self.calories
    
    def get_dictionary (self):
        return self.dictionary

    # Might not need this one 
    def change_name(self, new_name):
        self.name = new_name
     
    def change_calories (self, new_calorie):
        self.calories = new_calorie

    def choose(self, index):
        self.food_choice = self.food_list[index]
        self.name = self.food_choice.pop(NAME)
        self.brand = self.food_choice.pop(BRAND)
        self.calories = self.food_choice.pop(CALORIES)
        self.dictionary = self.food_choice
    # Method to add items to the dictionary. It returns -1 if there is an error 
    # or it returns 0 if it is able to add an item.


        








