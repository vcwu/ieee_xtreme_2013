import sys
import itertools
import collections
import math
# http://docs.python.org/2/library/itertools.html#itertools.combinations
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
    

def checkPalindrome(thingy):
	rev = thingy[::-1]
	if thingy==rev:
		return True
	return False
num = sys.stdin.readline().strip('\n')
meat = sys.stdin.readline().strip('\n')

combo = []
summ=0
#calulate firsts and seconds
summ += len(meat)

#first find how many groups of chars there is
counts  = dict(collections.Counter(meat))
print "counts" 
print counts
for key,value in counts.items():
	if value > 1:
		n_fact = (math.factorial(value))
		n_r_fact = math.factorial(value - 2)
		combos = float(n_fact)/((n_r_fact)*2)
		print "for value " + str(value)
		print "combo " + str(combos)
		summ += combos

for i in range(2,int(num)):
	thingy = list(combinations(meat,i+1))
	for i in thingy:
		thing = "".join(i)
		if checkPalindrome(thing):
			summ+=1

#summ=0
print int(summ)
