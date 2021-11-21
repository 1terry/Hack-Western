from flask import Flask,render_template,request, url_for
from person import person
from API import API
from FoodItem import FoodItem
from foodList import foodList
from meal import meal

app = Flask (__name__)
# CORS(app)

userInfo = []
currentFoods = []
nutritionInfo = {}
user = person("male", 1, 1, 1, "light")
mealList = []

@app.route ("/")
def home():
    return render_template('index.html',  
    data=[{'name':'little'},{'name':'light'},{'name':'moderate'},{'name':'hard'},{'name':'work'},{'name':'athlete'}])
    

@app.route('/toList', methods = ['GET', 'POST'])
def getList():
    if request.method == 'GET':
       print("Should never GET")

    if request.method == 'POST':
        form_data = request.form
        global currentFoods
        for key,value in form_data.items():
            foodItem = form_data.get('foodItem')
            currentFoods.append(foodItem)

            person.add_meal()
            person.calculate_daily_nutrient_profile()

        print(currentFoods)
        return render_template('index.html', selected_items = currentFoods, person_data = userInfo, scrollToAnchor='end')

                                        
@app.route('/foodData', methods = ['GET', 'POST'])
def foodData():
    if request.method == 'GET':
       print("Should never GET")
    if request.method == 'POST':
        foods = []
        foodNames = []
        foodNames.clear()
        foods.clear()
       
        form_data = request.form
        count = 0
        global currentFoods
        global nutritionInfo
        for key,value in form_data.items():
            if (count == 0):
                print(value)
                food_list = foodList(value)
                foods = food_list.return_list()
                for i in foods:
                    brandName = i.get_brand()
                    itemName = i.get_name()
                    foodName = itemName + ", brand: " + brandName
                    foodNames.append(foodName)
                    
                    
                # print("filler")
           
                # return_dictionary ["Food"] = value
            count = count + 1     
            # print(form_data)
            print("List of foods: " , foods)
            print("Foods" , foodNames)

        return render_template('index.html', form_data = foodNames, selected_items = currentFoods, person_data = userInfo, scrollToAnchor='end')
    




@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':

        form_data = request.form

        # We will create a list.
        return_dictionary = []

        # Temporary values for the given attributes.
        counter = 0
        sex = "male"
        height = 1
        weight = 1
        age = 1
        exercise_level = "NO"

        # This will be for if the user wishes to bulk, maintain, or lose weight
        condition = "losing"

        # Creating values for the user.
        for key, value in form_data.items():
            
            if counter == 0:
                print(value)
                age = int(value)
                return_dictionary.append("Age: " + str(age))
               
            
            elif counter == 1:
                print(request.form['gender'])
                sex = value
                return_dictionary.append("Sex: " + sex)
                
            
            elif counter == 2:
                height = int(value) 
                return_dictionary.append("Height: " +  str(height))
               
 
            elif counter == 3:
                weight = int(value)
                return_dictionary.append("Weight: " +  str(weight))

            elif counter == 4:
                exercise = request.form.get('exercise')
                exercise_level = exercise
                return_dictionary.append("Exercise: " + exercise_level)

            elif counter == 5:
                condition = value
                return_dictionary.append("Condition: " + condition)
            counter = counter + 1
    
        print("number of items: ", counter)
        # Create a temporary person with the given attributes 
        global user
        user.change_age(age)
        user.change_exercise_level(exercise_level)
        user.change_height(height)
        user.change_weight(weight)
        user.change_sex(sex)

        # Add the final condition that the user has selected.
        if (condition.lower() == "maintain"):
            return_dictionary ["Condition"] = user.return_maintenance()
        elif (condition.lower() == "bulk"):
            return_dictionary ["Condition"] = user.return_bulking()
        elif (condition.lower() == "losing"):
            return_dictionary.append("Maintenence Calorie Count: " + str(user.return_losing("moderate")))

        global userInfo 
        userInfo = return_dictionary

        # Returns a dictionary 
        return render_template('index.html', person_data = return_dictionary, scrollToAnchor='end')

 
app.run(host='localhost', port=5000)