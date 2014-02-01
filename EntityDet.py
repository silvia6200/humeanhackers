import nltk, re, pprint, Rel
# Splits ready Dataset 

def detectEnt(sentences):
	
	grammar = r"""
		NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
		PP: {<IN><NP>}               # Chunk prepositions followed by NP
		VB: {<VB.>+}				 # Chunk sequence of verbs
		VP: {<VB><NP|PP|CLAUSE>+$}   # Chunk verbs and their arguments
		CLAUSE: {<NP><VP>}           # Chunk NP, VP
		"""
	cp = nltk.RegexpParser(grammar, loop=2)
	
	# create a dictionary of chunks
	c = {}
	C = 0

	for sent in sentences
	
	IN = re.compile(r'.*\bin\b(?!\b.+ing)')
	OF = re.compile(r'.*\bof\b(?!\b.+ing)')	
	
	patterns = [IN,OF]
	
	for sentence in self.sentences:
	#entity detection and parsing
		sentne = nltk.ne_chunk(sentence, binary = True)	
		sentp = cp.parse(sentne)
		print("sentence parsed")
			for pattern in patterns:
				for rel in Rel.extract_rels('NE','NE',sentp, pattern, window = 10) 
			
		c[C] = 
		C = C+1
			
		
	print "Reached EOF"