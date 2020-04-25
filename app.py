from flask import Flask
from fastai.vision import *
from fast.mertics import error_rate
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'
