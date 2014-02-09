from neo4j import GraphDatabase
 
# Create a database
db = GraphDatabase("reldatabase")

def showAllNodes():
	number_of_nodes = len(db.nodes)
	print "This db has " + number_of_nodes +"nodes" 
	
	if(number_of_nodes>0):
		for node in db.nodes:
			print node + "\n"
	else: 
		print "no nodes"










db.shutdown()