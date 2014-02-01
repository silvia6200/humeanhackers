import ReadDataSet, SplitText


def extract(txtdoc):
	ReadDataSet.readD(txtdoc)
	SplitText.split(txtdoc + ".ready")