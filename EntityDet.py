import nltk, re, pprint
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

	for sent in sentences
	#entity detection - chunking
		sentnamed = nltk.ne_chunk(sent)
		sentchunk = cp.parse(sentnamed)
				
	# create a dictionary of chunks
	c = {}
	C = 0
		
	for sentence in self.sentences:
		c[C] = cp.parse(sentence)
		C = C+1
			
	#relation detection
		
		
		
	print "Reached EOF"