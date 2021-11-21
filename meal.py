"""
This is a meal class. It contains a list of food items.

November 19, 2021 
- Created class
"""
NAME = 'item_name'
BRAND = 'brand_name'
CALORIES = 'nf_calories'
from FoodItem import FoodItem
from foodList import foodList

class meal:
    # Constructor for the class
    def __init__(self, name):
        # List of food items
        self.__list_of_foods = []
        self.__name = name
        self.__calories = 0
        self.__nutrition_dictionary = {}

    # Adding food to the list. Returns -1
    # if the item is in the list and 0 if it added
    # and item successfully.
    def add_foods(self, new_food, index):
        food_list = foodList(new_food)

        food_dict = food_list.return_chosen(index)

        name = food_dict.pop(NAME)
        brand = food_dict.pop(BRAND)
        calories = food_dict.pop(CALORIES)

        self.__calories = self.__calories + float(calories)
        food_item = FoodItem(name, brand, calories, food_dict)

        if len(self.__nutrition_dictionary) == 0:
            self.__nutrition_dictionary = food_item.get_dictionary()
        else:
            for i in self.__nutrition_dictionary:
                if (i != 'nf_serving_size_unit') and (i != 'nf_serving_size_qty'):
                    if food_item.get_dictionary()[i] != 'null':
                        self.__nutrition_dictionary[i] = round(float(self.__nutrition_dictionary[i]), 2) + round(float(food_item.get_dictionary()[i]), 2)

        self.__list_of_foods.append(food_item)

    def get_name(self):
        return self.__name

    def get_food_list (self):
        return self.__list_of_foods

    # Returning a food item of the given name.
    # Returns a food item if found or None if none found.
    def find_food_item (self, food_name):

        # Loop through the list and find the item.
        for i in self.__list_of_foods:
            if i.get_name() == food_name:
                return i

        return None# No item found

    def total_cal(self):
        return self.__calories

    def return_nutrient_profile(self):
        return self.__nutrition_dictionary
