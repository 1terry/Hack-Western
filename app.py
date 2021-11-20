"""
This is the main class. It will host a local flask server and be responsible for bridging the gap between the frontend and the backend.
"""

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify 
from flask_cors import CORS # This should be fine after installing flask 
import json

app = Flask (__name__)
CORS(app)

@app.route ("/")
def home():
    return ("<h1>Welcome to the server</h1>")

@app.route('/api/', methods = ['POST'])
def postmethod():

    # We will need to get stuff from the frontend.

    return 0

if __name__ == "__main__":
    app.run(debug = True)