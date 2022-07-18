# Make a virtual environment and install flask:

# really good explanation of venv: https://www.youtube.com/watch?v=KxvKCSwlUv8

# 'which python3' get the path to your python3 executable
# 'cd flask_hello_world' navigate to the folder you want to rely on the venv
# ' /usr/bin/python3 -m venv venvName' create the venv with any name you want
# 'source venvName/bin/activate' activate the venv
# 'deactiave' will deactivate the venv

# you path now points to python3 and pip3 so you can run python or pip and they will refer to version 3
# `echo $PATH` you can see the path for dependecies 
# `pip install flask peewee` install flask and peewee into your virtual env

import os, base64
from flask import Flask, render_template, request, redirect, url_for, session
# import schema/ db object model for adding info to the sqlite db
from db.model import SavedTotal


app = Flask("myAppName")
app.secret_key = b'v]\x9a\xad\xc3\r\xd9g\x13n\xb6V\x99\x85\xfdK\xf2v\x92\x80\xd9\xb3M\x01'

@app.route('/add', methods=['GET', 'POST'])
def add():
    # if first time user visits page, initialize session total you can use the session because a random token was added to the secret_key value on app
    if 'total' not in session:
        session['total'] = 0

    # flask lets us see what kind of request was sent (Post, Put, Get, etc.)
    if request.method == 'POST':
        # access the form submitted: "<input type="number" id="number" name="number">" in add.jinja2
        number = int(request.form['number'] or 0) # cast to int, we don't know what the user entered (or to prevent cast error)
        session['total'] += number

    return render_template('add.jinja2', session=session) # inject entire session into our template as the session variable - add.jinja2 should retrieve this session value
    # if you don't set the templat session to our session variable, the total will not be passed through and will not increment

@app.route('/save', methods=['POST'])
def save():
    total = session.get('total', 0)
    # create a string of chars for the save total
    code = base64.b32encode(os.urandom(8)).decode().strip("=")

    # create a new entry using the db schema/model
    saved_total = SavedTotal(value=total, code=code)
    saved_total.save()
    # if you get a 500 internal error, make sure you have setup the db with python dbSetup.py
    # use sqliteStudio to see the table values in the db

    return render_template('save.jinja2', code=code)

@app.route('/retrieve')
def retrieve():
    # because the retrieve form uses the GET method, we have to use Flasks
    # request.args instead of the request.form
    # default value of None if they haven't submited the form yet
    retrieveCode = request.args.get('code', None)

    # If the suer is visiting the retrieve page (did not submit form yet):
        #Then just reder the retrieve.jinja2 template
    # But if they did submit the form:
        # Then attempt to retriee teh SavedTotal that has the provided code
        # Then save the total from that SavedTotal into the session['total']
        # Then redirect the user back to the main 'add' page
    if retrieveCode is None:
        return render_template('retrieve.jinja2')
    else:
        # try catch in case code doesn't exist in the db
        try:
            saved_total = SavedTotal.get(SavedTotal.code == retrieveCode)
        except SavedTotal.DoesNotExist:
            return render_template('retrieve.jinja2', error="Code not found")

        session['total'] = saved_total.value

        return redirect(url_for('add'))




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

# try to hit port 5000 on localhost, make sure you add the `/add` route - it's the only one defined

# Try it out:
# create a session key with some random data from python
# in the terminal (with venv activated) run:
# python
# import os
# os.urandom(24)
# assign the random key to the app.secret_key, now you can utilize the 'session' map for storing cookies



# Try it out:
# go to add route and increment numbers by adding, you will see the session persists across browser refreshes
# it will persist until the session is cleared
# save a and copy the saved id that is gernated
# increment the total some more in the session
# go to the retrieve route and enter the code: you will see that it sets the session total back to the value saved for that token
# try entering a bad code and you will see the error message