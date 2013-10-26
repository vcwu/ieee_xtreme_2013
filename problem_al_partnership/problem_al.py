import sys
import itertools

def checkPalindrome(thingy):
	rev = thingy[::-1]
	if thingy==rev:
		return True
	return False
num = sys.stdin.readline().strip('\n')
meat = sys.stdin.readline().strip('\n')

combo = []
for i in range(int(num)):
	combo.extend(list(itertools.combinations(meat,i+1)))

summ=0
for i in combo:
#	print str(i)
	thing = "".join(i)
	if checkPalindrome(thing):
		summ+=1
print summ
