import sys

def calculate(op1, op2, current):
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
	return ans


def parseStack(stack):
	otherStack = []


	while True:
		if len(stack) == 0:
			return otherStack
			break
		op = stack.pop(0)
		#print op
		if op not in  "+-&|~X":
			op = int(op,16)
			otherStack.append(op)

		else:
			if op == '~':
				cur = otherStack.pop()
				otherStack.append(~cur & 0xFFFF)
			else:
				op1 = 	otherStack.pop()
				op2 = 	otherStack.pop()
				ans = calculate(op1,op2,op)
				otherStack.append(ans)

line = sys.stdin.readline()
	
q = line.strip('\n').split(" ")
stack= [] 
try:
	stack= parseStack(q)
	if stack[0] > int("FFFF", base=16):
		stack[0]= int("FFFF", base=16)
	elif stack[0]< 0:
		stack[0] = 0 
	print "{0:04X}".format(stack[0])
except:
	print "ERROR"
