from neo4j import GraphDatabase
import shutil
 
workingdb = "reldatabase"
 
def addtodb(lnode, rnode, relationship):
	# Create a database
	db = GraphDatabase(workingdb)
	#	rel['subjsym'], rel['objsym'], rel['filler'] 

	with db.transaction:
		countquery = """START n=node(*) 	
						MATCH (n)
						WHERE HAS(n.name) AND n.name = {name}
						RETURN count(n)"""
		if  (int(str(db.query(countquery, name=lnode).single['count(n)'] )) == 0):
			leftnode = db.node(name=(lnode))
			print "Lnode " + lnode + "created"
		else:
			for node in db.nodes:
				for key, value in node.items():
					if (key == "name" and value == lnode):
						leftnode = node

		if  (int(str(db.query(countquery, name=rnode).single['count(n)'] )) == 0):
			rightnode = db.node(name=(rnode))
			print "Rnode " +rnode + "created"

		else:
			for node in db.nodes:
				for key, value in node.items():
					if (key == "name" and value == rnode):
						rightnode = node

		crquery = """START n=node(*)
					MATCH (n) - [r] -> m
					WHERE HAS(n.name) AND n.name = {nname} 
						  AND HAS(m.name) AND m.name = {mname}
						  AND TYPE(r) = {rel}
					RETURN count(r)"""
		if (int(str(db.query(crquery, nname=lnode, mname=rnode, rel=relationship).single['count(r)'] )) == 0):
			leftnode.relationships.create(relationship, rightnode)
			print "relationship " + relationship



		
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
			   WHERE HAS(n.name) AND n.name = {name}
			   RETURN n.name, r, m.name"""

	print db.query(query, name=qname)
	

	db.shutdown()