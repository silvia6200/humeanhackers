import nltk, re, pprint, EntityDet

# Splits ready Dataset

def split(self):
	
	#find basename
	import os
	base = os.path.basename(self)
		
	
	#read file
	with open (self,"r") as myfile:
		text = myfile.readlines()
		
	#sentence segmentation - done in read method
	#sentences = nltk.sent_tokenize(text)
		
	#tokenization
	sentences = [nltk.word_tokenize(sent) for sent in text]
	
	#pos tagging
	sentences = [nltk.pos_tag(sent) for sent in sentences]
		
	print(sentences[0])
		
	e = EntityDet.detectEnt(sentences)
		
