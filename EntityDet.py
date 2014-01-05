import nltk, re, pprint

class EntityDet:
	" " " Splits ready Dataset " " " 

	def __init__(self, file1):
		self.file1 = file1
		
	def detectEnt(self)
		
		#find basename
		import os
		base = os.path.basename(self.file1)
		
	
		#read file
		with open (self.file1,"r") as myfile:
			text = myfile.read()
			
		#entity detection
		
		#relation detection
		
		
		
		#write document
		with open(base + ".pos", "w") as mefile:
			mefile.writelines(text1)