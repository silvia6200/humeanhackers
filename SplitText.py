import nltk, re, pprint

# Splits ready Dataset

def split(txtreadydoc):
	
	#find basename
	import os
	base = os.path.basename(txtreadydoc)
		
	
	#read file
	with open (txtreadydoc,"r") as myfile:
		text = myfile.readlines()
		
	#sentence segmentation - done in read method
	#sentences = nltk.sent_tokenize(text)
		
	#tokenization
	sentences = [nltk.word_tokenize(sent) for sent in text]
	
	#pos tagging
	sentences = [nltk.pos_tag(sent) for sent in sentences]
		
	print(sentences[0])
		
	
