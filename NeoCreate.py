from neo4j import GraphDatabase
import shutil
 
workingdb = "reldatabase"
 
def addtodb(lnode, rnode, relationship):
	# Create a database
	db = GraphDatabase(workingdb)
	#	rel['subjsym'], rel['objsym'], rel['filler'] 

	with db.transaction:
		leftnode = db.node(name=(lnode))
		rightnode = db.node(name=(rnode))

		leftnode.relationships.create(relationship, rightnode)

	print "Created nodes " + lnode + " and " + rnode + " with relationship " + relationship +"! \n"

	db.shutdown()

def showAllNodes():

	# open the db
	db = GraphDatabase(workingdb)

	number_of_nodes = len(db.nodes)
	query = "START n=node(*) RETURN n"

	print "This db has " + str(number_of_nodes) +"nodes" 
	
	if(number_of_nodes>0):

		print db.query(query)
	else: 
		print "no nodes"
	
	db.shutdown()

def cleanDB():
	shutil.rmtree(workingdb)

def showAllDB():
	#open the db
	db = GraphDatabase(workingdb)

	query = """START n=node(*)
				MATCH (n) - [r] -> (m)
				RETURN n.name, r, m.name """

	print db.query(query)

	db.shutdown()

def showAllRelations(qname):
	db = GraphDatabase(workingdb)

	query = """START n=node(*)
			   MATCH (n) - [r] -> (m)
			   WHERE n.name = {name}
			   RETURN n.name, r, m.name"""

	print db.query(query, name=qname)