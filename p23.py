import time
import math

def sumOfDivisors(num):
	total = 1
	for x in range(2, math.floor(math.sqrt(num))+1):
		if(x*x == num):
			total += x
		elif(num%x == 0):
			total += (x + int(num/x))
	return total

def isAbundant(num):
	return num < sumOfDivisors(num)

t = time.time()

abundant_num = {}

for x in range(1, 28124):
	abundant_num[x] = isAbundant(x)

total = 0

for x in range(1, 28124):
	total += x
	for y in range(1, x):
		if(abundant_num[y] and abundant_num[x-y]):
			total -= x
			break

t = time.time() - t

print("\nThe sum of all nums not written as a sum of 2 abundant nums is %d\nTook %.3f seconds\n" % (total, t))