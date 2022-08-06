

# Make a virtual environment and install flask:

# really good explanation of venv: https://www.youtube.com/watch?v=KxvKCSwlUv8

# 'which python3' get the path to your python3 executable
# 'cd flask_hello_world' navigate to the folder you want to rely on the venv
# ' /usr/bin/python3 -m venv venvName' create the venv with any name you want
# 'source venvName/bin/activate' activate the venv
# 'deactiave' will deactivate the venv

# you path now points to python3 and pip3 so you can run python or pip and they will refer to version 3
# `echo $PATH` you can see the path for dependecies 
# `pip install flask` install flask into your virtual env

import os
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return "Hello World"

# pass query arguments into the route
@app.route('/hello/<name>')
def hello_name(name):
    return "Hello " + name

@app.route('/hello/<name>/<times>')
def hello_name_times(name, times):
    return (" Hello " + name) * int(times)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


# you can run the app: python main.py
# open postman or a browser and hit the hello route to get a response 
# `http://127.0.0.1:5000/hello/mark/3`