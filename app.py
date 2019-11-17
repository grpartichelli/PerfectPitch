from flask import Flask, request, render_template
import time 

from sound import *
from controller import *
from text import *
from utils import *

text = Text()
sound = Sound()
control = Controller()


app = Flask(__name__)

@app.route('/')
def my_form():
	return render_template('my-form.html', holder = "Insert notes here")

@app.route('/', methods=['POST'])
def my_form_post():
		input_string = request.form['text']
		instrument = request.form['dropdown'] 
		try:
			txt_file = request.files['myfile']
			if(len(txt_file.filename) > 1):
				input_string = str(txt_file.read())			
		#user didnt upload any filename
		except KeyError:
			pass
		
		#Gets the input text and parses it
		text.setText(input_string)
		notes = text.getParsed()

		#Sets the notes and instruments the control will play
		control.setInstrument(int(instrument) - 1)
		control.setNotes(notes)
		#Plays them
		control.playNotes()

		
		return render_template('my-form.html',holder = "Insert notes here")




#return processed_text
if __name__ == '__main__':
	app.run(debug = True,use_reloader = False)
