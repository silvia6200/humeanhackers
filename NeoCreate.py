from neo4j import GraphDatabase
import shutil
 
workingdb = "mannerdb"
 
def addtodb(lnode, rnode, relationship):
	# Create a database
	db = GraphDatabase(workingdb)
	#	rel['subjsym'], rel['objsym'], rel['filler'] 

	with db.transaction:
		
		lnodef = False	#lnodef and rnodef store whether the node has been found in the db
		rnodef = False
		for node in db.nodes:
				for key, value in node.items():
					if (key == "name"):
						if(value == lnode):
							leftnode = node
							lnodef = True	
						if(value == rnode):
							rightnode = node
							rnodef = True

		if (not lnodef):
			leftnode = db.node(name=(lnode))
			print "Lnode " + lnode + "created"

		if (not rnodef):
			rightnode = db.node(name=(rnode))
			print "Rnode " + rnode + "created"

		relf = False
		for rel in leftnode.relationships.outgoing:
			for key, value in rel.items():
				if (str(rel.type) == relationship and key == 'hits'and rel.end == rightnode):
					rel[key] = value + 1
					relf = True
					print "rel  found. Increasing number of hits "
		if (not relf):
			rel = leftnode.relationships.create(relationship, rightnode)
			print "created relationship " + relationship
			rel['hits'] = 1

		
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


def showAllRelations(qname):
	db = GraphDatabase(workingdb)


	query = """START n=node(*)
			   MATCH (n) - [r] -> (m)
			   WHERE HAS(n.name) AND n.name = {name}
			   RETURN n.name, r, m.name"""

	print db.query(query, name=qname)


	db.shutdown()

def showAllDB():
	db = GraphDatabase(workingdb)

	query = """START n=node(*)
				MATCH (n) - [r] -> (m)
				RETURN n.name, r, m.name"""

	print db.query(query)

	db.shutdown()
