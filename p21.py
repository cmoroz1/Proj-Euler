import time
import math

def d(n):
	total = 1
	for x in range(2, math.ceil(math.sqrt(n))+1):
		if(x*x == n):
			total += x
		elif(n%x == 0):
			total += x
			total += n/x
	return int(total)

t = time.time()

total = 0

amicable_pairs = {}

for x in range(1, 10000):
	a = d(x)
	if(d(a) == x and x != a and x not in list(amicable_pairs.values())):
		amicable_pairs[x] = a
		total += a + x

t = time.time() - t

print("\nThe sum of all amicable numbers below 10,000 is %d\nTook %.3f seconds\n" % (total, t))

print(amicable_pairs)