"""
This is the person class. We will do bodily calculations with this class.

November 19, 2021
- Created class
"""
from meal import meal


class person:
    # Constructor
    def __init__ (self, sex, height, weight, age, exercise_level):
        self.sex = sex
        self.height = height
        self.weight = weight
        self.age = age
        self.exercise_level = exercise_level
        self.meal_list = [meal('Meal 1'), meal('Meal 2'), meal('Meal 3')]
        self.total_cal = 0
        self.nutrition_profile = {}

    def change_sex (self, new_sex):
        self.sex = new_sex

    def get_sex (self):
        return self.sex

    def change_height (self, new_height):
        self.height = new_height

    def get_height (self):
        return self.height
    
    def change_weight (self, new_weight):
        self.weight = new_weight

    def get_weight (self):
        return self.weight
    
    def change_age (self, new_age):
        self.age = new_age
    
    def get_age (self):
        return self.age
    
    def change_exercise_level (self, new_level):
        self.exercise_level = new_level
    
    def return_exercise_level (self):
        return self.exercise_level
    
    # Private method that will return the bmr given the specifications of the person.
    def __get_bmr (self):
        
        # Calculate bmr for a male
        if self.sex == "male":
            return (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        
        elif self.sex == "female":
            return (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161

        else:
            return -1
    
    # Return the maintenance calories for the person.
    def return_maintenance (self):
    
        if self.exercise_level == "little":
            return int(self.__get_bmr() * 1.2)

        elif self.exercise_level == "light":
            return int(self.__get_bmr() * 1.4)

        elif self.exercise_level == "moderate":
            return int(self.__get_bmr() * 1.6)

        elif self.exercise_level == "hard":
            return int(self.__get_bmr() * 1.75)

        elif self.exercise_level == "work":
            return int(self.__get_bmr() * 2.0)

        elif self.exercise_level == "athlete":
            return int(self.__get_bmr() * 2.4)

        else:
            return -1

    # Return the bulking calories.
    def return_bulking (self):
        return int(self.return_maintenance() * 1.10)

    # Return the calories for losing.
    # "moderate": 5% decrease in calories
    # "insane": 10% decrease in calories
    def return_losing (self, lose_rate):

        if lose_rate == "moderate":
            return int(self.return_maintenance() * 0.95)
        
        elif lose_rate == "insane":
            return int(self.return_maintenance() * 0.90)

        # An error occurred.
        else:
            return -1

    def add_meal(self, index):
        self.meal_list.insert(index-1, meal('Meal' + index))
        new_index = index
        while new_index < len(self.meal_list):
            self.meal_list[index].change_name(3)

    def remove_meal(self, index):
        self.meal_list.pop(index)

    def return_meal_at(self, index):
        return self.meal_list[index]

    def return_meals(self):
        return self.meal_list

    def calculate_missing_cal_maintenance(self):
        return self.return_maintenance() - self.calculate_total_cal()

    def calculate_missing_cal_losing(self):
        return self.return_losing() - self.calculate_total_cal()

    def calculate_missing_cal_bulking(self):
        return self.return_bulking() - self.calculate_total_cal()

    def calculate_total_cal(self):
        for i in self.meal_list:
            self.total_cal = self.total_cal + i.total_cal()
        return self.total_cal

    def calculate_daily_nutrient_profile(self):
        for i in self.meal_list:
            if len(self.nutrition_profile) == 0:
                if len(i.return_nutrient_profile()) != 0:
                    self.nutrition_profile = i.return_nutrient_profile()
            else:
                if len(i.return_nutrient_profile()) != 0:
                    for j in i.return_nutrient_profile():
                        if (j != 'nf_serving_size_unit') and (j != 'nf_serving_size_qty'):
                            self.nutrition_profile[j] = round(float(self.nutrition_profile[j]), 2) + round(float(i.return_nutrient_profile()[j]), 2)
        return self.nutrition_profile
