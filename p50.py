import time

t = time.time()

print("Calculating primes...")
limit = 1000000
arr = [True]*limit
def sieve(x):
    global arr, limit
    for i in range(x*2, limit, x):
        arr[i] = False
for x in range(2, limit//2):
    sieve(x)
primes = [i for i in range(2, limit) if arr[i]]

maximum_length = 0
maximum_prime = 0
for i in range(len(primes)):
    total = 0
    for j in range(i, len(primes)):
        total += primes[j]
        if(total < 1000000 and arr[total] and j-i > maximum_length):
            maximum_length = j-i
            maximum_prime = total
        if(total > 1000000):
            break

print("The prime below 1,000,000 that can be written as the sum")
print("of consecutive primes is %d with the length of %d" % (maximum_prime, maximum_length))
print("Took %.3f seconds" % (time.time() - t))