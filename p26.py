from decimal import *
import time

t = time.time()

def findRepeatLen(num):
	s = num[2:]
	for x in range(len(s)//2):
		for y in range(1, (len(s)-x)//2):
			part1 = s[x:x+y]
			part2 = s[x+y:x+2*y]
			if(part1 == part2):
				# Introduced an extra check to 
				# make sure terms were repeating
				part3 = s[x+2*y:x+3*y]
				if(part2 == part3):
					return len(part1)

precision = 500

getcontext().prec = precision

max_repeat = 0
number = 0

for x in range(2, 1000+1):
	num = str(Decimal(1)/Decimal(x))
	if(len(num) < 2+precision):
		continue
	repeat = findRepeatLen(num)
	while(repeat == None):
		precision += 500
		getcontext().prec = precision
		num = str(Decimal(1)/Decimal(x))
		repeat = findRepeatLen(num)
	if(repeat > max_repeat):
		max_repeat = repeat
		number = x

t = time.time() - t

print("\n1/%d has a recurring cycle of %d\nPrecision went up to %d decimal places\nTook %.3f seconds\n" % (number, max_repeat, precision, t))