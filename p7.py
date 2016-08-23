limit = 200000
arr = [True]*limit
def sieve(x):
	global arr, limit
	for i in range(x*2, limit, x):
		arr[i] = False
for x in range(2, limit//2):
	sieve(x)
primes = [i for i in range(2, limit) if arr[i]]

print("\nThe 10,001st prime is", primes[10001-1], "\n")