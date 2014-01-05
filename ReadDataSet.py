class ReadDataSet:
	" " " Reads the given Dataset " " " 

	def __init__(self, file1):
		self.file1 = file1
		
	def readD(self)
		
		#find basename
		import os
		base = os.path.basename(self.file1)
		
	
		#read file
		with open (self.file1,"r") as myfile:
			text = myfile.read()
			
		#extract relevant text from dataset
		text1 = 
		
		#write document
		with open(base + ".ready", "w") as mefile:
			mefile.writelines(text1)
		