import sys
numHills = int(sys.stdin.readline().strip('\n'))

speeds = map(int, sys.stdin.readline().strip('\n').split())
speeds.reverse()

sumSpeeds = []
sumSpeeds.append(0)	#start at finish line

largest = 0

for i in speeds:
	summ = sumSpeeds[-1] + i
	sumSpeeds.append(summ)
	if summ > largest:
		largest = summ

print largest

