primes = []

def isPrime(num, primes):
	if(len(primes) == 0):
		return True
	for x in primes:
		if(num%x == 0):
			return False
	return True

total = 0

for x in range(2, 2000001):
	if(isPrime(x, primes)):
		primes.append(x)
		total += x

print("\nThe sum of all primes below 2,000,000 is %d\n" % (total))