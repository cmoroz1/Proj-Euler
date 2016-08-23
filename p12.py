import math
import time

def genTriNum(x):
	return (x*(x+1))/2

def numFactors(x):
	if(x == 1): return 1
	count = 0
	for i in range(1, math.ceil(math.sqrt(x))):
		if(x%i == 0):
			count += 2
		if(i*i == x):
			count -= 1
	return count

start = time.time()

numDivisors = 0

count = 70
while(numDivisors <= 500):
	count += 1
	numDivisors = numFactors(genTriNum(count))

end = time.time()

print("\nThe first triangle number with over 500 divisors is %d. Took %.3f seconds\n" % (genTriNum(count), end - start))