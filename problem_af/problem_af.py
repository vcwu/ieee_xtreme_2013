import sys
num= int(sys.stdin.readline().strip('\n'))
desired = []
for i in range(num):
	desired.append(int(sys.stdin.readline().strip('\n')))
#generate the entire list thingy
thingy = {}

improved= {}

for i in range(1337):
	thingy[i + 1] = []

for i in range(1000):
	improved[i+1] = 0 	# num i yell out -> [where I should stand for that number]

#print str(thingy[1])
counter = 1 #what is current person's position
up = True
for i in range(max(desired)): 
	yelling = i+ 1
	
	improved[yelling] = counter
	thingy[counter].append(yelling)	
	if "7" in str(yelling):
		#say number and switch
		up = not up	
	elif yelling%7 == 0:
		#say number and switch
		up = not up

	if up:
		if counter == 1337:
			counter = 1
		else:
			counter += 1
	else:	
		if counter == 1:
			counter = 1337
		else:
			counter -= 1

#print desired

#print "desired stuffs"
for i in desired:
	print improved[i]
