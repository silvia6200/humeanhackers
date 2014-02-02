from __future__ import print_function
import nltk, re, pprint, EntityDet, os

# Splits ready Dataset

def split(txtreadydoc):
	
	#find basename
	base = os.path.basename(txtreadydoc)
		
	
	#read file
	with open (txtreadydoc,"r") as myfile:
		bla = myfile.read()
	
	text = nltk.sent_tokenize(bla)
	l = len(text)
	print("length of dataset: "+ (str(l)))
	#sentence segmentation - done in read method
	#sentences = nltk.sent_tokenize(text)
	c1 = 0
	dict = {}
	#tokenization
	for sent in text:
		dict[c1] = nltk.word_tokenize(sent[:-1] + 'in Germany.')
		c1 += 1
		print( (str(c1)), end='\r') 
		
	print("sentences tokenized")
	#pos tagging
	c2 = 0
	sentences =[]
	for sent in dict:
		blub = nltk.pos_tag(dict[sent])
		sentences += [blub]
		c2 += 1
		print( (str(c2)), end='\r')
		print(blub)
	#sentences = [nltk.pos_tag(sent) for sent in sentences]
	print("sentences tagged")
	
	EntityDet.detectEnt(sentences)
		
	
