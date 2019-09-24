import glob
from pygame import mixer
import time

class Sound():
  def __init__(self):
    mixer.init()
    self.dic = {}
    self.octave = 4
    self.volume = 1.0
    self.tempo = 1.0
    
    for note in glob.glob("./Music_Note/piano2/*.ogg"):
      #excludes path and extension from file
      name = note[20:-4]
      name = name.upper()
      self.dic[name] = mixer.Sound(note)


  def play(self,note):
    note = note + str(self.octave)
    note = self.dic[note]
    print(self.volume)
    note.set_volume(self.volume)
    note.play()
    time.sleep(self.tempo)
  
  
  def increaseOctave(self):
    if self.octave >= 0 and self.octave < 7:
      self.octave += 1

  def decreaseOctave(self):
    if self.octave > 0 :
      self.octave -= 1

  def increaseVolume(self):
    if self.volume <= 8:
      self.volume += 1.5
  
  def decreaseVolume(self):
    if self.volume >= 1.5:
      self.volume -= 1.5

  def increaseTempo(self):
    self.tempo += 0.3

  def decreaseTempo(self):
    self.tempo -= 0.3
  
  def restart(self):
    self.octave = 4
    self.volume = 1.0



class Interface():
  def playText(self,sound,sequence):
    sound.restart()

    for i in range(0,len(sequence)):
      key = sequence[i]
      key = key.upper()
      
      try:
        nextKey = sequence[i+1]
      except:
        nextKey = -1
      
      if key == '+':
        sound.increaseVolume()
      
      elif key == '-':
        sound.decreaseVolume()
      
      elif key == 'O':
        #octave
        if nextKey == '+':
          sound.increaseOctave()
        if nextKey == '-':
          sound.decreaseOctave()     
        
      try:
        sound.play(key)
      except:
        pass
  

if __name__ == '__main__':
  UI = Interface()
  sound = Sound()
  UI.playSequence(sound,'CCC+++DDD---EEEO+FFF')
