# import flask dependency
from flask import Flask
# Create a new flask app
app = Flask(__name__)
# add a root
@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/product/<name>')
def get_product(name):
    return "The product is " + str(name)