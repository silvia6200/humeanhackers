import ReadDataSet, SplitText, EntityDet

def extract(txtdoc,reads):
	if reads:
		ReadDataSet.readD(txtdoc)
		print("document read")
		splits = SplitText.split(txtdoc + ".ready", True)
		print("document split")
		EntityDet.detectEnt(splits)
		print("entites detected")

	else:
		splits = SplitText.split(txtdoc, False)
		print("document split")
		EntityDet.detectEnt(splits)
		print("entites detected")