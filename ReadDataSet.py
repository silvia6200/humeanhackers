from __future__ import print_function

#Reads the given Dataset 
		
def readD(txtdoc):
		
	#find basename
	import os, nltk
	base = os.path.basename(self)		
			#read file
	with open (self,"r") as myfile:
		text = myfile.readlines()
		
	#extract relevant text from dataset
				
	#write document
	f = open(base + ".ready", "w")         
		
			
	#counts loops
	a = 0
			
	#for every line
	for line in text:
							 
		if line.startswith("<bestanswer>"):
				
		#split line into sentences
			sentences = nltk.sent_tokenize(line[12:-13])
				
			s = len(sentences)
			#write into document
			x=0
			while x < (s-1):
				f.write(sentences[x] + "\n")
				a +=1
				x+=1
			f.write(sentences[s-1])
					
			a +=1
			print( (str(a)), end='\r') 
				
	f.close
        