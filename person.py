"""
This is the person class. We will do bodily calculations with this class.

November 19, 2021
- Created class
"""

class person:

    # Constructor
    def __init__ (self, sex, height, weight, age, exercise_level):
        self.sex = sex
        self.height = height
        self.weight = weight
        self.age = age
        self.exercise_level = exercise_level

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
        if (self.sex == "male"):
            return ((10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5)
        
        elif (self.sex == "female"):
            return ((10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161)

        else:
            return -1
    
    # Return the maintenance calories for the person.
    def return_maintenance (self):
    
        if (self.exercise_level == "little"):
            return (int(self.__get_bmr() * 1.2))

        elif (self.exercise_level == "light"):
            return (int(self.__get_bmr() * 1.4))

        elif (self.exercise_level == "moderate"):
            return (int(self.__get_bmr() * 1.6))

        elif (self.exercise_level == "hard"):
            return (int(self.__get_bmr() * 1.75))

        elif (self.exercise_level == "work"):
            return (int(self.__get_bmr() * 2.0))

        elif (self.exercise_level == "athlete"):
            return (int(self.__get_bmr() * 2.4))

        else:
            return -1

    # Return the bulking calories.
    def return_bulking (self):
        return (int(self.return_maintenance() * 1.10))

    # Return the calories for losing.
    # "moderate": 5% decrease in calories
    # "insane": 10% decrease in calories
    def return_losing (self, lose_rate):

        if (lose_rate == "moderate"):
            return (int(self.return_maintenance() * 0.95))
        
        elif (lose_rate == "insane"):
            return (int(self.return_maintenance() * 0.90))

        # An error occurred.
        else:
            return -1