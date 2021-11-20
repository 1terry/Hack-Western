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
    
    def getName (self):
        return self.name
    
    def getCalories (self):
        return self.calories
    
    def getDictonary (self):
        return self.dictonary

    # Might not need this one 
    def changeName(self, newName):
        self.name = newName
     
    def changeCalories (self, newCalorie):
        self.calories = newCalorie
    
    # Method to add items to the dictionary. It returns -1 if there is an error 
    # or it returns 0 if it is able to add an item.
    def addItem (self, newItem, newItemValue):
        
        # If the value is in the dictionary already
        if (newItem in self.dictonary):
            return -1

        # We can add the item and its value
        else:
            self.dictionary [newItem] = newItemValue
            return 0
        








