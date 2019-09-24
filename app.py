from flask import Flask, request, render_template
from note import *
import time 

sound = Sound()
UI = Interface()
app = Flask(__name__)

@app.route('/')
def my_form():
	return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['text']
	processed_text = text.upper()
	instrument = request.form.get('instruments')
	print(instrument)
	UI.playText(sound,processed_text)
	time.sleep(5)
	return render_template('my-form.html')


#return processed_text


if __name__ == '__main__':
	app.run(debug = True,use_reloader = True)
