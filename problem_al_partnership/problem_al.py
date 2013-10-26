import sys
import itertools

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
for i in range(int(num)):
	thingy = list(combinations(meat,i+1))
	for i in thingy:
		thing = "".join(i)
		if checkPalindrome(thing):
			summ+=1

#summ=0
print summ
