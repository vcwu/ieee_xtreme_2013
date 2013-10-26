import sys

thing = sys.stdin.readline().strip("\n") 
row, col = thing.split()
row = int(row)
col = int(col)
#print row
#print col

bigTable = []

for i in range(int(row)):
	thing = sys.stdin.readline().strip("\n") 
	thing = thing.split()
	bigTable.append([int(x) for x in thing])

#swappy thing
swapped = []
swapped = bigTable
#for i in bigTable:
#	swapped.insert(0,i)

#print "actual data"
#for i in swapped:
	#print i

currentRow = row -2  #start at row 1

summedRisks = []
lst = []
for i in range(col):
	lst.append((i,(i,i)))
summedRisks.append(lst)

while currentRow >= 0 :
	curRowMeat = []
	for currentCol,risk in enumerate(swapped[currentRow]):
		#edge cases
		risks = []
		if currentCol == 0:
			risks.append((0,swapped[currentRow+1][0]))
			risks.append((1,swapped[currentRow+1][1]))
		elif currentCol == (col-1):
			risks.append((col-1,swapped[currentRow+1][col-1]))
			risks.append((col-2,swapped[currentRow+1][col-2]))
		else:
			risks.append((currentCol-1,swapped[currentRow+1][currentCol-1]))
			risks.append((currentCol,swapped[currentRow+1][currentCol]))
			risks.append((currentCol+1,swapped[currentRow+1][currentCol+1]))
		smallestRiskCell=  min(risks, key=lambda item:item[1])
		smallestRisk = risk + smallestRiskCell[1]
		locPrevCell = (currentRow+1, smallestRiskCell[0])
		#rewrite with smallest risk
		swapped[currentRow][currentCol] = smallestRisk
		curRowMeat.append((smallestRisk, locPrevCell))
	currentRow-=1
	summedRisks.insert(0,curRowMeat)

#print "MEAT MEAT" 
#for i in summedRisks:
	#print i

#FIND THE MIN ROUTE :D :D

#so first, find the minimum # on the top row, then follow down to the bottom
#if there are even weights, we need to go from left most first
path = []

topSmallestCol = 0
smallest = summedRisks[0][0][0]
for index, value in enumerate(summedRisks[0]):
	if value[0] < smallest:
		smallest = value[0]
		topSmallestCol =  index

#print "smallest " + str(smallest)
#print "smallestCol " + str(topSmallestCol)
	

#smallestRiskCell = min(summedRisks[-1], key = lambda item:item[0])
#print "smallestRiskCell "  + str(smallestRiskCell)
#print "locPrev " + str(locPrev)
path.append((0,topSmallestCol)) #this is where we came from
locPrev = summedRisks[0][topSmallestCol][1]
path.append(locPrev)
while True:
	
	climbingRow = locPrev[0]
	nextCol = locPrev[1]
	locPrev = summedRisks[climbingRow][nextCol][1]
	#print "locPRev inloop " + str(locPrev)
	path.append(locPrev)
	if climbingRow == row-2:
		break

#for i in path:
#	print i

meat = "Minimum risk path = "
#path.reverse()
for i in path:
	thingy = "[" + str(i[0]) + "," + str(i[1]) + "]"
	meat += thingy
print meat
print "Risks along the path = " + str(smallest)
