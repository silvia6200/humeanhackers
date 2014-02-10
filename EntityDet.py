from __future__ import print_function
import nltk, re, pprint, Rel, WLemmatizer
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
	#IS = re.compile(r'.*\bis\b(?!\b.+ing)(?!\b.+/VBN).*')   insert IS to patterns when uncommenting
	TO = re.compile(r'.*\bto\b(?!\b.+ing)')
	AND = re.compile(r'.*\band\b')

	VB = re.compile(r'.*\b/VB\b(?!\b.+ing)(?!\b.+/VBN)')     # Base form
	VBD = re.compile(r'.*\b/VBD\b(?!\b.+ing)(?!\b.+/VBN)')	 # past tense
	VBG = re.compile(r'.*\b/VBG\b')							 # present participle or gerund
	VBN = re.compile(r'.*\b(has|have|had)(((?!been).*/VBN)|(been.*(?!\b.+/VBN)))')			 # has + have past participle
	VBZ = re.compile(r'.*\b/VBZ\b(?!\b.+ing)(?!\b.+/VBN)')	 # present 3rd Sg
	VBP = re.compile(r'.*\b/VBP\b(?!\b.+ing)(?!\b.+/VBN)')	 # present not 3rd Sg
	VBPA = re.compile(r'.*\b/VBN.*\bby\b')					# passive
	
	patterns = [IN,OF, TO,AND]
	pnames = ["IN","OF","TO","AND"]
	#write document
	vpatterns = [VB, VBD, VBG, VBN, VBP, VBZ,VBPA]
	vnames = ["/VB", "/VBD", "/VBG","/VBN","/VBP","/VBZ","/VBN"]
	f = open("testentities1", "w") 


	#number of relations
	r= 0
	print("Number of relations found: ")
	for sentence in sentences:
	#entity detection and parsing
		sentne = nltk.ne_chunk(sentence, binary = True)	
		sentp = cp.parse(sentne)
		#print(sentne)

		ps = 0
		vps = 0
		
		for pattern in patterns:
			#print("me here")

			for rel in Rel.extract_rels('NE','NE', sentne, pattern, 10): 
				#print("and here")
				#NeoCreate.addtodb(rel)
				f.write(pnames[ps] + " Relation:  " + nltk.sem.relextract.show_raw_rtuple(rel) + '\n')
				r += 1
				print( (str(r)), end='\r') 
				
			ps+= 1

		for vpattern in vpatterns:
			rno = 0
			for rel2 in Rel.extract_rels('NE','NE',sentne, vpattern, 10 ):
				fillers = rel2['filler'].split()
				verb = [v for v in fillers if v.endswith(vnames[vps])]		# gets the verbs that matches the patterns
				verbl = WLemmatizer.lmtz(verb[0])

				if vpattern == VBPA:
					ssym = rel2['subjsym']
					stext = rel2 ['subjtext']
					rel2['subjsym'] = rel2['objsym']
					rel2['objsym'] = ssym
					rel2['subjtext'] = rel2['objtext']
					rel2['objtext'] = stext

				f.write(verbl[:(verbl.find('/'))] + " Relation:  " + nltk.sem.relextract.show_raw_rtuple(rel2) + '\n')
				r+=1
			vps+= 1
			
	print(str(r))
			
	f.close
	

	