from neo4j import GraphDatabase
 
# Create a database
db = GraphDatabase(reldatabase)
 
def addtodb(rel):
#	rel['subjsym'], rel['objectsym'], rel['filler'] 
	
	relationship = rel['filler']

	#cleaning the filler of everything after the slash
	if(relationship.find('/')>0)
		relationship = relationship[0:relationship.find('/')]

	with db.transaction:
		rightnode = db.node(name=rel['subjsym'])
		leftnode = db.node(name=rel['objectsym'])


		





# All write operations happen in a transaction
# with db.transaction:
#     firstNode = db.node(name='Hello')
#     secondNode = db.node(name='world!')
 
#     # Create a relationship with type 'knows'
#     relationship = firstNode.knows(secondNode, name='graphy')
 
# Read operations can happen anywhere
# message = ' '.join([firstNode['name'], relationship['name'], secondNode['name']])
 
# print message
 
# Delete the data
# with db.transaction:
#     firstNode.knows.single.delete()
#     firstNode.delete()
#     secondNode.delete()
 
# Always shut down your database when your application exits
# db.shutdown()