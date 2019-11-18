class Text():
	text = ""
	parsed = []
	def __init__(self):
		pass
	#Sets the text
	def setText(self,text): 
		self.text = text.upper()

	#Parses the text to a list
	def parseText(self):
		self.parsed = list(self.text)

	#Return the parsed text
	def getParsed(self):
		self.parseText()
		return self.parsed 
	
#TESTING
if __name__ == "__main__":
  text = Text()
  text.setText("something")
  print(text.getParsed())