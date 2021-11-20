from API import API


class foodList:
    api = API()
    food_list = []

    def __init__(self, food_name):
        self.food_list = self.api.call_api(food_name)

    def return_chosen(self, index):
        return self.food_list[index]

    def return_list(self):
        return self.food_list
