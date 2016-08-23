import time
import math

t = time.time()

primes = {}

def isPrime(num):
	if(num in list(primes.keys())):
		return primes[num]
	for x in range(2, int(math.sqrt(num))+1):
		if(num%x == 0):
			primes[num] = False
			return False
	primes[num] = True
	return True

def digitRotations(num):
	num = str(num)
	lst = []
	for x in range(len(num)):
		lst.append(int(num[x:] + num[:x]))
	return lst

def isCircularPrime(num):
	lst = digitRotations(num)
	for x in lst:
		if(not isPrime(x)):
			return False
	return True

maximum = 10**6

lst = []

for x in range(2, maximum):
	if(isCircularPrime(x)):
		lst.append(x)

t = time.time() - t

print("\nThere are %d circular primes below 1,000,000" % (len(lst)))
print("Took %.3f seconds\n" % (t))