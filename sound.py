import pygame.midi
from midiutil.MidiFile import MIDIFile
from constants import *



class Sound():
   
  def __init__(self):
    pygame.init()
    self.track = 0   # the only track
    self.time = 0    # start at the beginning
    self.channel = 0 #channel to be played
    self.volume = 31 # volume of the note
    self.duration =0.5 #note duration
    self.instrument= 0 
    self.octave = 0
    self.mf = MIDIFile(1) 
    self.mf.addTrackName(self.track, self.time, "Sample Track")

    #tempo = 100
    self.mf.addTempo(self.track, self.time, 100)
    pass 
  

  def increaseInstrument(self, number):
    self.instrument = self.instrument + number
    if (NOTE_B + self.octave*12) > 127:
      self.instrument = 0

  def increaseOctave(self):
    self.octave = self.octave + 1
    if (NOTE_B + self.octave*12) > 127:
      self.octave = 0

  #Sound cant be bigger than 127
  def doubleVolume(self):
    if self.volume*2 <= 127:
      self.volume = self.volume*2
    else:
      self.volume = 31
      
  

  #Define instrument
  def setInstrument(self,instrument):
    self.instrument = instrument

  #Writes a note to the midi object
  def addNote(self,note):
    self.time = self.time + 1
    self.mf.addProgramChange(self.track, self.channel, self.time, self.instrument)
    self.mf.addNote(self.track, self.channel, note + self.octave*12, self.time, self.duration, self.volume)
  
  #Writes the midi object to a midi file
  def writeFile(self):
    with open("output.mid", 'wb') as outf:
      self.mf.writeFile(outf)
  

  #Plays the midi file
  def playFile(self):
    #Loads file
    pygame.mixer.music.load("output.mid")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
      pygame.time.wait(1000)