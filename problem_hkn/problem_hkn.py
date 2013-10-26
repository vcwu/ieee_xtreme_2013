import sys
thingy = sys.stdin.readline()

lower,upper = thingy.strip('\n').split(',')


lower = int(lower)
upper = int(upper)

li = range(lower,upper+1)

palindromeList = []

numPalin = 0
for num in li:
	thingy = bin(num)[2:]
	rev = thingy[::-1]
	if thingy==rev:
		numPalin+=1
print numPalin
