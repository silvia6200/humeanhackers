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
		sentences = nltk.sent_tokenize
		
		#tokenization
		
		#pos tagging
		
		
		
		#write document
		with open(base + ".pos", "w") as mefile:
			mefile.writelines(text1)