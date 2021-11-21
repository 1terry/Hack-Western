from flask import Flask,render_template,request, url_for
from person import person
from API import API
from FoodItem import FoodItem
from foodList import foodList
from meal import meal

app = Flask (__name__)
# CORS(app)

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
                                        
@app.route('/foodData', methods = ['GET', 'POST'])
def foodData():
    if request.method == 'GET':
       print("Should never GET")
    if request.method == 'POST':
        foods = []
        foodNames = []
        form_data = request.form
        count = 0
        for key,value in form_data.items():
            if (count == 0):
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

        


        return render_template('index.html', form_data = foodNames, scrollToAnchor='end')
    

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':

        form_data = request.form

        # We will create a dictionary.
        return_dictionary = {}

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
        for key,value in form_data.items():
            
            if counter == 0:
                age = int(value)
                return_dictionary ["Age"] = age
               
            
            elif counter == 1:
                print(request.form['gender'])
                sex = value
                return_dictionary ["Sex"] = sex
                
            
            elif counter == 2:
                height = int(value) 
                return_dictionary ["Height"] = height
               
 
            elif counter == 3:
                weight = int(value)
                return_dictionary ["Weight"] = weight

            elif counter == 4:
                exercise = request.form.get('exercise')
                exercise_level = exercise
                return_dictionary ["Exercise Level"] = exercise_level

            elif counter == 5:
                condition = value
                return_dictionary ["Condition"] = condition
            counter = counter + 1
    
        print("number of items: ", counter)
        # Create a temporary person with the given attributes 
        Kohei = person(sex, height, weight, age, exercise_level)

        # Add the final condition that the user has selected.
        if (condition.lower() == "maintain"):
            return_dictionary ["Condition"] = Kohei.return_maintenance()
        elif (condition.lower() == "bulk"):
            return_dictionary ["Condition"] = Kohei.return_bulking()
        elif (condition.lower() == "losing"):
            return_dictionary ["Maintenance Calories"] = Kohei.return_losing("moderate")

        # Returns a dictionary 
        return render_template('data.html', form_data = return_dictionary)

 
app.run(host='localhost', port=5000)