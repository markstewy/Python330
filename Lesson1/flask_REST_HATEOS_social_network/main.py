# Repo setup:
# which python3
# /usr/bin/python3 -m venv venv
# source venv/bin/activate


from ast import Store
from functools import cache
from nis import match
import os
from types import SimpleNamespace
from flask import Flask, Response, make_response, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    request.content_type
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

# RESTFUL request format:
# content_type
# content_length
# last_modified
# If-None-Match
# If-Match (and or) If-Unmodified-Since

# if you want the API to not cache, use:
#     no-cache
#     no-store
#     pragma: no-cache
#     Expires: 0


# RESTULF response format:
def makeResponse() -> Response:
    res = make_response("hi")
    res.content_type()          # https://flask.palletsprojects.com/en/2.1.x/api/#flask.Response.content_type
    res.content_length()        # https://flask.palletsprojects.com/en/2.1.x/api/#flask.Response.content_length
    res.last_modified()         # https://flask.palletsprojects.com/en/2.1.x/api/#flask.Response.last_modified
    res.add_etag("asdf")        # https://flask.palletsprojects.com/en/2.1.x/api/#flask.Response.add_etag
    res.location()              # https://flask.palletsprojects.com/en/2.1.x/api/#flask.Response.location
    res.cache_control()         # https://flask.palletsprojects.com/en/2.1.x/api/#flask.Response.cache_control
    res.expires()               # https://flask.palletsprojects.com/en/2.1.x/api/#flask.Response.expires
    res.date()                  # https://flask.palletsprojects.com/en/2.1.x/api/#flask.Response.date





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

