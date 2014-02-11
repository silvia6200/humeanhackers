import ReadDataSet, SplitText, EntityDet, NeoCreate

def extract(txtdoc,reads,clean):
#reads = true if the document has to be read in or in other words ReadDataSet has to be run over the document
	if clean: 
		NeoCreate.cleanDB()
	if reads:
		ReadDataSet.readD(txtdoc)
		print("document read.")
		splits = SplitText.split(txtdoc + ".ready", True)
		print("document has been split.")
		EntityDet.detectEnt(splits)
		print("entity detection completed.")

	else:
		splits = SplitText.split(txtdoc, False)
		print("document has been split.")
		EntityDet.detectEnt(splits)
		print("entity detection completed.")

	NeoCreate.showAllNodes()

