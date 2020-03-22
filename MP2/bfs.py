# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 
import boto3
# This class represents a directed graph 
# using adjacency list representation 

def storeindb(graphdata):
    dynamodb = boto3.resource('dynamodb')
    distancetable = dynamodb.create_table(
     TableName = 'citydata',
     KeySchema = 
     [{
         'AttributeName' : 'fcityname',
         'KeyType' : 'Hash'
      },
      {
          'AttributeName' : 'scityname',
          'KeyType' : 'Range'
      }
     ],
     AttributeDefinitions =
     [
         {
             'AttributeName' : 'fcityname',
             'AttributeType' : 'S'
         },
         {
             'AttributeName' : 'scityname',
             'AttributeType' : 'S'
         },
         {
            'AttributeName' : 'distance',
            'AttributeType' : 'S'
         }

     ]   
    )
    distancetable.meta.client.get_waiter('table_exists').wait(TableName='citydata')
    print(distancetable.item_count)

    return



class Graph: 

	# Constructor 
	def __init__(self): 

		# default dictionary to store graph 
		self.graph = defaultdict(list) 

	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	# Function to print a BFS of graph 
	def BFS(self, s): 

		# Mark all the vertices as not visited 
		visited = dict()
		distancearray = dict()

		# Create a queue for BFS 
		queue = list() 

		# Mark the source node as 
		# visited and enqueue it 
		queue.append(s) 
		visited[s] = True
		
		#create a distance variable
		distance = 0

		while queue: 

			# Dequeue a vertex from 
			# queue and print it 
			temp = queue.pop(0) 
			#print (temp) 

			# Get all adjacent vertices of the 
			# dequeued vertex s. If a adjacent 
			# has not been visited, then mark it 
			# visited and enqueue it 
			for i in self.graph[temp]: 
				distance = distance + 1
				if not(i in visited.keys()): 
					queue.append(i) 
					distancearray[i] = distance
					visited[i] = True
				
			
		return distancearray
# Driver code 

# Create a graph given in 
# the above diagram 
g = Graph() 
node = dict()
g.addEdge("india", "canada") 
node["india"]=1;
node["cananda"]=1;
g.addEdge("canada", "usa") 
node["canada"]=1;
node["usa"]=1;
g.addEdge("usa","luxemburg") 
#node["usa"]=1;
#ode["india"]=1


print ("Following is Breadth First Traversal"
				" (starting from vertex 2)") 
#g.BFS("canada") 
DistanceGraph = dict()


for i in node.keys():
	distance = g.BFS(i)
	#print(i)
	#print("1" + str(i))
	DistanceGraph[i]=distance

print("reached here")
for i in DistanceGraph.keys():
	for k in DistanceGraph[i].keys():
		print(i)
		print(k)
		print(DistanceGraph[i][k])

storeindb(DistanceGraph)
		
  
    


