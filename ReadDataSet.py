from __future__ import print_function

class ReadDataSet:
	" " " Reads the given Dataset " " " 

	def __init__(self, file1):
		self.file1 = file1
		
	def readD(self):
		
		#find basename
		import os, nltk
		base = os.path.basename(self.file1)		
	
		#read file
		with open (self.file1,"r") as myfile:
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
        