

import glob
from pygame import mixer
import time


class Sound():
  def __init__(self):
    mixer.init()
    self.dic = {}
    self.octave = 4
    for note in glob.glob("./Music_Note/piano2/*.ogg"):
      #excludes path and extension from file
      name = note[20:-4]
      name = name.upper()
      self.dic[name] = mixer.Sound(note)


  def play(self,note,vol = 1):
    note = note + str(self.octave)
    note = self.dic[note]
    note.set_volume(vol)
    note.play()
    time.sleep(1.1)


  def increaseOctave(self):
    if self.octave >= 0 and self.octave < 7:
      self.octave += 1

  def decreaseOctave(self):
    if self.octave > 0 :
      self.octave -= 1






class Interface():
  def playSequence(self,sound,sequence):
    volume = 0.8
    for i in range(0,len(sequence)):
      key = sequence[i]
      key = key.upper()
      try:
        nextKey = sequence[i+1]
      except:
        nextKey = -1
      
      if key == '+':
        volume = volume * 2
      
      elif key == '-':
        volume = volume/2
      
      elif key == 'O':
        #octave
        if nextKey == '+':
          sound.increaseOctave()
        if nextKey == '-':
          sound.decreaseOctave()    
      else:
        try:
          sound.play(key,volume)
        except:
          pass #nope
      


if __name__ == '__main__':
  UI = Interface()
  sound = Sound()
  UI.playSequence(sound,'CCC+++DDD---EEEO+FFF')
