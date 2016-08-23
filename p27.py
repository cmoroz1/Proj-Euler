import time
import math

t = time.time()

def isPrime(num):
	if(num < 0): num *= -1
	if(num == 1): return False
	if(num == 2): return True
	for x in range(2, int(math.sqrt(num))+1):
		if(num%x == 0):
			return False
	return True

def consecutivePrimes(a, b):
	prime = True
	n = -1
	while(prime):
		n += 1
		num = n**2 + a*n + b
		prime = isPrime(num)
	# Return N-1 because it failed on N
	# so it worked up to N-1
	return n-1

prime_lst = []

for x in range(2, 1001):
	if(isPrime(x)):
		prime_lst.append(x)

cons_count = 0
a_val = 0
b_val = 0

#
# EQUATION IS n^2 + an + b
#
for b in prime_lst:
	for a in range(1000):
		#TEST BOTH POSITIVE
		count = consecutivePrimes(a, b)
		if(count > cons_count):
			cons_count = count
			a_val = a
			b_val = b

		#TEST A NEGATIVE
		count = consecutivePrimes(-a, b)
		if(count > cons_count):
			cons_count = count
			a_val = -a
			b_val = b
		#B must be positive because when n=0
		#a prime number must be produced

t = time.time() - t

print("\nThe coefficients a: %d and b: %d produce the longest consecutive primes\nfrom 0 to %d. Their product, a*b, is %d" % (a_val, b_val, cons_count, a_val*b_val))
print("Took %.3f seconds\n" % (t))