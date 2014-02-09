from __future__ import print_function
import nltk, re, pprint, Rel,NeoCreate
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
	
	

	IN = re.compile(r'.*\bin\b(?!\b.+ing)')
	OF = re.compile(r'.*\bof\b(?!\b.+ing)')
	IS = re.compile(r'.*\bis\b(?!\b.+ing)')
	TO = re.compile(r'.*\bto\b(?!\b.+ing)')
	AND = re.compile(r'.*\band\b')
	VB = re.compile(r'.*\b/VB.*\b.*')
	
	patterns = [IN,OF,IS,TO,AND,VB]
	pnames = ["IN","OF","IS","TO","AND","VB"]
	#write document
	f = open("testentities", "w") 


	#number of relations
	r= 0
	print("Number of relations found: ")
	for sentence in sentences:
	#entity detection and parsing
		sentne = nltk.ne_chunk(sentence, binary = True)	
		sentp = cp.parse(sentne)
		#print(sentne)

		ps = 0
		
		for pattern in patterns:
			#print("me here")

			for rel in Rel.extract_rels('NE','NE', sentne, pattern, 10): 
				print("and here")
				NeoCreate.addtodb(rel)
				#NeoCreate.addtodb(rel)
				f.write(pnames[ps] + "Relation:  " + nltk.sem.relextract.show_raw_rtuple(rel) + '\n')
				r += 1
				print( (str(r)), end='\r') 
				print(rel)
			ps+= 1
	print(str(r))
			
	f.close
	

	