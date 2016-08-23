count = 0
primes = []
num = 2

while(count != 10001):
	if(len(primes) == 0):
		primes.append(num)
		num += 1
		count += 1
	else:
		prime = True
		for x in primes:
			if(num % x == 0):
				prime = False
		if(prime):
			primes.append(num)
			count += 1
		num += 1

print("\nThe 10,001st prime is", primes[len(primes)-1], "\n")