from flask import Flask
from fastai.vision import *

import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'
