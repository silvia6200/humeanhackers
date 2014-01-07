import nltk, re, pprint

class EntityDet:
	" " " Splits ready Dataset " " " 

	def __init__(self, sentences):
		self.sentences = sentences
	
	def detectEnt(self):
		
		#entity detection - chunking

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
		
		for sentence in self.sentences:
			c[C] = cp.parse(sentence)
			C = C+1
			
		#relation detection
		
		
		

		print "Reached EOF"