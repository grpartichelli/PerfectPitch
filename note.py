

import glob
from pygame import mixer
import time


class Note():
  def __init__(self):
    print("init\n\n")
    mixer.init()
    self.dic = {}
    for note in glob.glob("./Music_Note/piano/*.wav"):
      #excludes path and extension from file
      name = note[19:-4]
      self.dic[name] = mixer.Sound(note)


  def play(self,note):
    note = note.upper()
    note = self.dic[note]
    note.play()
    time.sleep(1.5)


class Interface():
  def playSequence(self,note,sequence):
    for key in sequence:
      note.play(key)
    



if __name__ == '__main__':
  UI = Interface()
  sound = Note()
  UI.playSequence(sound,'CCCDDDEEEFFF')
