NOTE_C = 60
NOTE_D = 62
NOTE_E = 64
NOTE_F = 65
NOTE_G = 67
NOTE_A = 69
NOTE_B = 71


def getSequence(file):
        with open(file) as f:
                firstLine = f.readline()
        if(len(firstLine) > 0):
                return firstLine
        else:
                return -1
