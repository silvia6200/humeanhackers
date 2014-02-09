from neo4j import GraphDatabase
 
# Create a database
db = GraphDatabase("reldatabase")
 
def addtodb(rel):
#	rel['subjsym'], rel['objectsym'], rel['filler'] 
	
	relationship = rel['filler']

	#cleaning the filler of everything after the slash
	if(relationship.find('/')>0):
		relationship = relationship[0:relationship.find('/')]

	with db.transaction:
		rightnode = db.node(name=(rel['subjsym']+""))
		leftnode = db.node(name=(rel['objsym']+""))

		leftnode.relationships.create(relationship, rightnode)

	print "Created nodes " + rel['subjsym'] + " and " + rel['objsym'] + " with relationship " + rel['filler'] +"! \n"

	db.shutdown()

def showAllNodes():
	number_of_nodes = len(db.nodes)
	print "This db has " + number_of_nodes +"nodes" 
	
	if(number_of_nodes>0):
		for node in db.nodes:
			print node + "\n"
	else: 
		print "no nodes"
	db.shutdown()

