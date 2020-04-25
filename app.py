from fastai.vision import *
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import requests

app = Flask(__name__)

@app.route("/post_field", methods=["GET", "POST"])
def need_input():
    for key, value in request.form.items():
        print("key: {0}, value: {1}".format(key, value))

@app.route("/form", methods=["GET"])
def get_form():
    return render_template('index.html')
   
@app.route('/')
def hello_world():
   return 'Hello, World!'

def show_path():
   path = Path(os.getcwd())
   return(path)

   
