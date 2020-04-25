from fastai.vision import *
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def get_url():
	return(render_template('get_url.html'))

@app.route('/show_result', methods=['POST', 'GET'])
def show_result():
	if request.method == 'POST':
		url = request.form['url']
		path = Path(os.getcwd())
		learn = load_learner(path)
		import requests
		f = open('00000001.jpg','wb')
		link = input()
		f.write(requests.get(link).content)
		prediction = learn.predict(open_image(Path(os.getcwd())/'00000001.jpg'))
		f.close()
		return(render_template('show_result.html', url = url, path = path, prediction = prediction))
   
