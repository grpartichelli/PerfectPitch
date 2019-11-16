from flask import Flask, request, render_template
import time 

from sound import *
from controller import *
from text import *

text = Text()
sound = Sound()
control = Controller()


app = Flask(__name__)

@app.route('/')
def my_form():
	return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():

		input_string = request.form['text']
		instrument = request.form['dropdown'] 


		#Gets the input text and parses it
		text.setText(input_string)
		notes = text.getParsed()

		#Sets the notes and instruments the control will play
		control.setInstrument(int(instrument) - 1)
		control.setNotes(notes)
		#Plays them
		control.playNotes()

		
		return render_template('my-form.html')


#return processed_text
if __name__ == '__main__':
	app.run(debug = True,use_reloader = True)
