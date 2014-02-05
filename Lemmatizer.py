from __future__ import print_function
from nltk.stem.wordnet import WordNetLemmatizer
import nltk

def lmtz(textdoc):

	
	#find basename
	import os, nltk
	base = os.path.basename(textdoc)		
			#read file
	with open (textdoc,"r") as myfile:
		text = myfile.readlines()
		
	print("document read")
	#extract relevant text from dataset
				
	#write document
	f = open(base + ".lm", "w")         

	wl = WordNetLemmatizer()
			
	#counts loops
	a = 0
	l = len(text)
			
	#for every line
	for line in text:
		sentence = ""
		words = nltk.word_tokenize(line)
		print(words)
		wordss = nltk.pos_tag(words)
		for (word,tag) in wordss:
			if tag.startswith('V'):
				sentence += " " + wl.lemmatize(word,'v')
			else:
				sentence += " " + wl.lemmatize(word)
			
		f.write(sentence + "\n")			
		a +=1
		print( (str(a) + "of" + (str(l))), end='\r') 
				
	f.close