import time

t= time.time()

primes = []

limit = 2000000
arr = [True]*limit
def sieve(x):
	global limit, arr
	for i in range(x*2, limit, x):
		arr[i] = False
for x in range(2, limit//2):
	sieve(x)
primes = [i for i in range(2, limit) if arr[i]]

total = sum(primes)

print("\nThe sum of all primes below 2,000,000 is %d\n" % (total))
print("Took %.3f seconds" % (time.time() - t))