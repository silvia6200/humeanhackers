import ReadDataSet, SplitText, EntityDet 

textsource = "manner100.txt"

r = ReadDataSet.ReadDataSet(textsource)
r.readD()

s = SplitText.SplitText(textsource + ".ready")
s.split()