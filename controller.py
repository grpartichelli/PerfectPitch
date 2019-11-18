from sound import *
from utils import *


class Controller():
	instrument = 0
	notes = []

	def __init__(self):
		pass

	def setInstrument(self, instrument ):
		self.instrument = instrument

	def setNotes(self, notes):
		self.notes = notes

	def playNotes(self,filename):
		sound = Sound()
		sound.setInstrument(self.instrument)

		counter = 0
		for i,note in enumerate(self.notes):

			if note == 'A':
				sound.addNote(NOTE_A)
				
				continue
			
			if note == 'B':
				sound.addNote(NOTE_B)
				
				continue
			
			if note == 'C':
				sound.addNote(NOTE_C)
				
				continue
			
			if note == 'D':
				sound.addNote(NOTE_D)
				
				continue
			
			if note == 'E':
				sound.addNote(NOTE_E)
				
				continue
			
			if note == 'F':
				sound.addNote(NOTE_F)
				
				continue
			
			if note == 'G':
				sound.addNote(NOTE_G)
				
				continue

			if note == " ":
				sound.doubleVolume()
				 
				continue

			if note == "\n":
				sound.setInstrument(14) #Tubular Bells
				 
				continue

			if note == ";":
				sound.setInstrument(75) #Pan Flute
				 
				continue

			if note == "!":
				sound.setInstrument(133) #Agogo
				 
				continue

			if note == ",":
				sound.setInstrument(20) #Church Organ
				
				continue

			if note == "?":
				sound.increaseOctave() 
				 
				continue

			if note == "U" or note == "I" or note == "O" or note == "u" or note == "i" or note == "o":
				sound.setInstrument(6) #Harpischord
				 
				continue
			
			#Testing if the current character is a number
			if ord(note) >= 48 and ord(note) <= 57:
				sound.increaseInstrument(int(note)) 
				 
				continue

			#ELSE
			if i != 0:
				#Checks if its a char from A to G
				if ord(self.notes[i-1]) >=65 and ord(self.notes[i-1]) <= 71:
					note = self.notes[i-1]
					if note == 'A':
						sound.addNote(NOTE_A)
					if note == 'B':
						sound.addNote(NOTE_B)
					if note == 'C':
						sound.addNote(NOTE_C)   
					if note == 'D':
						sound.addNote(NOTE_D)
					if note == 'E':
						sound.addNote(NOTE_E)
					if note == 'F':
						sound.addNote(NOTE_F)
					if note == 'G':
						sound.addNote(NOTE_G)
				continue
			
			
		sound.writeFile(filename)
		sound.playFile(filename)
		



#TESTING
if __name__ == "__main__":
	control = Controller()
	#Sets the notes and instruments the control will play
	control.setInstrument(0)
	control.setNotes(['A','U',' ','A','^'])
	#Plays them
	control.playNotes()