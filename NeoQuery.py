from neo4j import GraphDatabase
 
# Create a database
db = GraphDatabase('reldatabase')

def showAllNodes:
	nodes = getNodes(db)
	for node in nodes:
		print node + "\n"










db.shutdown()