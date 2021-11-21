from flask import Flask,render_template,request
from person import person
from API import API
from FoodItem import FoodItem
from meal import meal

app = Flask (__name__)
# CORS(app)

@app.route ("/")
def home():
    return render_template('testForm.html')

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
        condition = ""

        # Creating values for the user.
        for key,value in form_data.items():
            
            if counter == 0:
                sex = value
                return_dictionary ["Sex"] = sex
            
            elif counter == 1:
                height = int(value) 
                return_dictionary ["Height"] = height
            
            elif counter == 2:
                weight = int(value)
                return_dictionary ["Weight"] = weight
 
            elif counter == 3:
                age = int(value)
                return_dictionary ["Age"] = age

            elif counter == 4:
                exercise_level = value
                return_dictionary ["Exercise Level"] = exercise_level

            elif counter == 5:
                condition = value
            counter = counter + 1
    
        # Create a temporary person with the given attributes 
        Kohei = person(sex, height, weight, age, exercise_level)

        # Add the final condition that the user has selected.
        if (condition.lower() == "maintain"):
            return_dictionary ["Condition"] = Kohei.return_maintenance()
        elif (condition.lower() == "bulk"):
            return_dictionary ["Condition"] = Kohei.return_bulking()
        elif (condition.lower() == "losing"):
            return_dictionary ["Condition"] = Kohei.return_losing("moderate")

        # Returns a dictionary 
        return render_template('data.html', form_data = return_dictionary)

 
app.run(host='localhost', port=5000)