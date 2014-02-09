from neo4j import GraphDatabase
 
# Create a database
db = GraphDatabase('reldatabase')

def showAllNodes():
	
	for node in db.nodes:
		print node + "\n"










db.shutdown()