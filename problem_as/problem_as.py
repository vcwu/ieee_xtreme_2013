import sys


def move(currentPath, dest, roads):
	#base case

	#print "Current Path " + str(currentPath)
	currentNode = currentPath[-1]
	for neighbor in roads[currentNode]:
		#print "\tCurrent Node " + currentNode
		#print "\tlooking at neighbor " + neighbor
		if neighbor in dest:
			#print "\t\tFOUND and appended! " + str(currentPath)
			temp = currentPath[:]
			temp.append(neighbor)
			allPossiblePaths.append(temp)
		elif neighbor not in currentPath:
			temp = currentPath[:]
			temp.append(neighbor)
			#print "\t\tCalling move again "  + str(currentPath)
			move(temp, dest, roads) 
		
	

dest = sys.stdin.readline()


roads = {}

while True:
	pair = sys.stdin.readline().strip('\n').split(" ")
	#print pair
	if pair[0] == 'A' and  pair[1] == 'A':
		break
	else:
		if pair[0] not in roads.keys():
			li = [pair[1]]
			roads[pair[0]] = li
		else:
			roads[pair[0]].append(pair[1])
		if pair[1] not in roads.keys():
			li = [pair[0]]
			roads[pair[1]] = li
		else:
			roads[pair[1]].append(pair[0])


#find ALL
#find shortest path from F to dest

stk = []
allPossiblePaths = []
stk.append("F")	#start stuff

move( stk, dest, roads)

allPossiblePaths.sort()
#print allPossiblePaths
if len(allPossiblePaths) != 0:
	#need to check if there is posible path
	minSize = len(allPossiblePaths[0])
	#minList = allPossiblePaths[0]
	minList = []
	for thing in allPossiblePaths:
		if len(thing) < minSize:
			minSize = len(thing)
			minList = thing



	#print roads
	print "Total Routes: " + str(len(allPossiblePaths))
	print  "Shortest Route Length: " + str(len(minList))
	last= "Shortest Route after Sorting of Routes of length " + str(len(minList)) + ":"
	for it in minList:
		last = last + " " + it
	print last
else:
	thing  = "No Route Available from F to " + dest.strip('\n') 
	print thing

