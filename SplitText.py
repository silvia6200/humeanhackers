from __future__ import print_function
import nltk, re, pprint, EntityDet, os

# Splits ready Dataset

def split(txtreadydoc, lined):
	
	#find basename
	base = os.path.basename(txtreadydoc)
	

	# if File has been cleaned to be one sentence per line:

	if lined:
		with open (txtreadydoc,"r") as myfile:
				text = myfile.readlines()
	else:
	#read file and tokenize sentence
		with open (txtreadydoc,"r") as myfile:
			bla = myfile.read()
		text = nltk.sent_tokenize(bla)
		print("documents read.")



	l = len(text)
	print("length of dataset: "+ (str(l)))


	#sentence segmentation - done in read method
	#sentences = nltk.sent_tokenize(text)
	c1 = 0
	dict = {}
	#tokenization
	print("Number of sentences tokenized:")
	for sent in text:
		dict[c1] = nltk.word_tokenize(sent[:-1] + ' in Germany.')
		c1 += 1
		print( (str(c1)), end='\r')
	print ( str(c1)) 
		
	print("sentence tokenizing completed.")


	f = open("tagged sentences", "w") 

	#pos tagging
	c2 = 0
	sentences =[]
	for sent in dict:
		blub = nltk.pos_tag(dict[sent])
		sentences += [blub]
		c2 += 1
		print( (str(c2)), end='\r')
		for (word,tag) in blub:
			f.write(" " + word + "/" + tag)
			#'print(e)
		f.write("\n")

	#sentences = [nltk.pos_tag(sent) for sent in sentences]
	print("sentence tagging completed.")
	
	f.close

	#EntityDet.detectEnt(sentences)
	return sentences
		
	
