import nltk, re, pprint

class EntityDet:
	" " " Splits ready Dataset " " " 

	def __init__(self, file1):
		self.file1 = file1
		
	def detectEnt(self):
		
		#find basename
		import os
		base = os.path.basename(self.file1)
		
	
		#read file
		with open (self.file1,"r") as myfile:
			text = myfile.read()
			
		#entity detection - chunking
		print nltk.ne_chunk(text, binary=True) # named entity extraction
		
		grammar = r"""
			NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
			PP: {<IN><NP>}               # Chunk prepositions followed by NP
			VB: {<VB.>+}				# Chunk sequence of verbs
			VP: {<VB><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
			CLAUSE: {<NP><VP>}           # Chunk NP, VP
			"""
		cp = nltk.RegexpParser(grammar, loop=2)
		
		# create a dictionary of chunks
		c = {}
		C = 0
		
		for sentence in text:
			c[C] = cp.parse(sentence)
			C = C+1
			
		#relation detection
		
		
		
		#write document
		with open(base + ".pos", "w") as mefile:
			mefile.writelines(text1)