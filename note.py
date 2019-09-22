

import glob
from pygame import mixer
import time


class Sound():
  def __init__(self):
    print("init\n\n")
    mixer.init()
    self.dic = {}
    for note in glob.glob("./Music_Note/piano/*.wav"):
      #excludes path and extension from file
      name = note[19:-4]
      self.dic[name] = mixer.Sound(note)


  def play(self,note,vol = 1):
    note = self.dic[note]
    note.set_volume(vol)
    note.play()
    time.sleep(1.1)


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
        if nextKey == '+':
          print("octave upper")
        if nextKey == '-':
          print("octave lowe")
     
      else:
        sound.play(key,volume)
      
      


if __name__ == '__main__':
  UI = Interface()
  sound = Sound()
  UI.playSequence(sound,'CCC+++DDD---EEEO+FFF')
