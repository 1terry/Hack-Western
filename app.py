"""
This is the main class. It will host a local flask server and be responsible for bridging the gap between the frontend and the backend.

November 19, 2021
- Created app class

Good resources:
https://stackoverflow.com/questions/22947905/flask-example-with-post

"""

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify 
from flask_cors import CORS # This should be fine after installing flask 
import json

app = Flask (__name__)
CORS(app)

# If the end of the web url is empty then this is the home screen.
@app.route ("/")
def home():
    return ("<h1>Welcome to the server</h1>")


# We need to change depending on the ending of the URL given. Or we can enforce url changes by using URL rule.

@app.route('/api/', methods = ['ACCOUNT', 'MODIFYACCOUNT', 'ADDMEAL', 'MODIFYMEAL', 'DELETEMEAL'])
def postmethod():


    # If the request is an account creation.
    if request.method == 'ACCOUNT':


    # If the server wants to change something about the account
    elif request.method == 'MODIFYACCOUNT':


    # If the server wants to add a meal
    elif request.method == 'ADDMEAL':
    

    # If the server wants to modify a meal
    elif request.method == 'MODIFYMEAL'


    # If the server wishes to delete a meal.
    elif request.method == 'DELETEMEAL'


    # We will send something to the server if there is some other request being made.
    else:
        return -1

if __name__ == "__main__":
    app.run(debug = True)