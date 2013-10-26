import sys

stack = []

#if the stack is only one thing
#	that's our answer, we're done
#reading from input thing one at a atime
#if that thing is a number puh it on
#if that thing is a operator pop off two of them


line = sys.stdin.readline()
#for char in sys.stdin.read():
#	if char == ' ' or char== '\n':
#		pass
#	else:
#		stack.append(char)
	
stack = line.strip('\n').split(" ")
	

#print stack
while True:
	if len(stack) == 1:
		break
	else:
		current = stack.pop()
		ans = 0
		if str(current) in "+-&|~X":
			op1 = int(stack.pop(), base=16)
			#print "op1 " + str(op1)
			if current == '~':
				#print "not"
				ans = not op1
			else:

				op2 = stack.pop()
				#print op2;
				op2 = int(op2, base=16)
				#print "op2 " + str(op2)
				if current == '+':
					ans = op1 + op2	

				if current == '-':
					ans = op2 - op1	
				if current == '&':
					ans = op1 & op2
				if current == '|':
					ans = op1 | op2
				if current == 'X':
					ans = op1 ^ op2
			#print ans
			stack.append(ans)


ans = stack[0] 
if stack[0] > int("FFFF", base=16):
	ans = int("FFFF", base=16)
elif stack[0]< 0:
	ans = 0 
print "{0:04X}".format(ans)
