import nltk, re, pprint

class SplitText:
	" " " Splits ready Dataset " " " 

	def __init__(self, file1):
		self.file1 = file1
		
	def split(self)
		
		#find basename
		import os
		base = os.path.basename(self.file1)
		
	
		#read file
		with open (self.file1,"r") as myfile:
			text = myfile.read()
			
		#sentence segmentation
		sentences = nltk.sent_tokenize(text)
		
		#tokenization
		sentences = [nltk.word_tokenize(sent) for sent in sentences]
		
		#pos tagging
		sentences = [nltk.pos_tag(sent) for sent in sentences]
		
		
		#write document
		with open(base + ".pos", "w") as mefile:
			mefile.writelines(text1)