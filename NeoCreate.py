from neo4j import GraphDatabase
 
# Create a database
db = GraphDatabase('reldatabase')
 
def addtodb(rel):
#	rel['subjsym'], rel['objectsym'], rel['filler'] 
	
	relationship = rel['filler']

	#cleaning the filler of everything after the slash
	if(relationship.find('/')>0):
		relationship = relationship[0:relationship.find('/')]

	with db.transaction:
		rightnode = db.node(name=rel['subjsym'])
		leftnode = db.node(name=rel['objectsym'])

		leftnode.relationships.create(relationship, rightnode)

	print "Created nodes " + leftnode + " and " + rightnode + " with relationship " + relationship +"! \n"

	db.shutdown()

