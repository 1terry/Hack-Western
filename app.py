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

@app.route ("/")
def home():
    return ("<h1>Welcome to the server</h1>")

@app.route('/api/', methods = ['ACCOUNT', 'MODIFYACCOUNT', 'ADDMEAL', 'MODIFYMEAL'])
def postmethod():
    

    # If the request is an account creation.
    if request.method == 'ACCOUNT':


    # If the server wants to change something about the account
    elif request.method == 'MODIFYACCOUNT':


    # If the server wants to add a meal
    elif request.method == 'ADDMEAL':
    

    # If the server wants to modify a meal
    elif request.method == 'MODIFYMEAL'

    # We will need to get stuff from the frontend.

    return 0

if __name__ == "__main__":
    app.run(debug = True)