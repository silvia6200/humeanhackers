import nltk, re, pprint, EntityDet

class SplitText:
	" " " Splits ready Dataset " " " 

	def __init__(self, file1):
		self.file1 = file1
		
	def split(self):
		
		#find basename
		import os
		base = os.path.basename(self.file1)
		
	
		#read file
		with open (self.file1,"r") as myfile:
			text = myfile.readlines()
			
		#sentence segmentation - done in read method
		#sentences = nltk.sent_tokenize(text)
		
		#tokenization
		sentences = [nltk.word_tokenize(sent) for sent in text]
		
		#pos tagging
		sentences = [nltk.pos_tag(sent) for sent in sentences]
		
		print(sentences[0])
		
		e = EntityDet.EntityDet(sentences)
		e.detectEnt()
		
