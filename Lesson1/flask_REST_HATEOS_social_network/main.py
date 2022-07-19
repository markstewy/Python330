# Repo setup:
# which python3
# /usr/bin/python3 -m venv venv
# source venv/bin/activate


import os
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # if token no in session redirect to /login
    # else redirect to home
    return json.dumps({"response": "flask is working"})

@app.route("/login", methods=["POST"])
def index():
    # provide link to createAcccount
    # if username and token match, set session token and go to home
    # else return error msg
    return 

@app.route("/createAccount", methods=["POST"])
def index():
    # include link to login
    # if username and password created, redirect to login
    # if username exists, redirect to login with error msg
    return 
    
@app.route("/home", methods=["GET", "POST"])
def index():
    # if no user session redirect to login
    # GET list friends and non friends
    # POST send invite to non friend
    # POST accept invite
    return

@app.route("/friend", methods=["GET", "POST"])
def index():
    # GET: show user partial data, if user already invited, disable invite
    # POST: Send friend request to user
    return






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)