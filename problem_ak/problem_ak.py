import sys

roads = {}
def findPath(start, end):
	#dfs on roads from star to end

	def bfs(G, s):
	    P, Q = {s: None}, deque([s]) 
	    while Q:
		u = Q.popleft() 
		for v in G[u]:
		    if v in P: continue 
		    P[v] = u 
		    Q.append(v)
	    return P

def findBottleneck(startNode, endNode, potentials):
	li = findPath(startNode, endNode)
	if len(potentials) == 0:
		potentials = li[:]
		print "adding to potentials"
		print str(potentials)
	else:
		potentials = list(set(potentials).intersection(set(li)))
		print "sub from potentials"
		print str(potentials)
	return potentials
	

meat = []  #please work
count = int(sys.stdin.readline().strip('\n'))-1

start = []
while count > 0:
	pair = map(int,sys.stdin.readline().strip('\n').split(" "))
	#print pair
	if pair[0] == 'A' and  pair[1] == 'A':
		break
	else:
		if pair[0] not in roads.keys():
			li = [pair[1]]
			roads[pair[0]] = li
			start.append(pair[0])
		else:
			roads[pair[0]].append(pair[1])
			if pair[1] in start:
				start.remove(pair[1])
		if pair[1] not in roads.keys():
			li = []
			roads[pair[1]] = li

	
	count -=1

#find start and end nodes
end = []
for key,value in roads.items():
	if len(value) == 0:
		end.append(key)


#find all possible combos from start to end
potentials = []
for startNode in start:
	for endNode in end:
		potentials = findBottleneck(startNode, endNode, potentials)

print "answer is "
for i in potentials:
	print i

print "Roads: map: " 
print str(roads)

print "Starts node"
for i in start:
	print i

print "End nodes"
for i in end:
	print i
