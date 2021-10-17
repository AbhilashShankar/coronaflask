from flask import Flask
from flask import render_template 
from .coviddata import data

app = Flask(__name__)





@app.route('/')
def say_name():
    return render_template('elements.html',data=data)