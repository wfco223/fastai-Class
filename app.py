from fastai.vision import *
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/post_field", methods=["GET", "POST"])
def need_input():
    url = request.args['url']
   
@app.route('/')
def hello_world():
   return 'Hello, World!'

def show_path():
   path = Path(os.getcwd())
   return(path)

   
