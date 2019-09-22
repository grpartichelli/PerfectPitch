

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


  def play(self):
    note = self.dic['A']
    note.play()
    time.sleep(5)






if __name__ == '__main__':
  sound = Note()
  sound.play()
