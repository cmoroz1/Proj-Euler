import time, math

t = time.time()

print("Calculating primes...")
limit = 1000000
arr = [True]*limit
def sieve(x):
    global arr, limit
    for i in range(x*2, limit, x):
        arr[i] = False
for i in range(2, limit//2):
    sieve(i)
primes = [x for x in range(2, limit) if arr[x]]

def testNum(num, primes):
    for p in primes:
        if(num-p <= 0):
            return False
        test = math.sqrt((num-p)/2)
        if(int(test) == test):
            return True
    return False

print("Testing numbers...")
number = 33
while(True):
    number += 2
    if(number > 10000000):
        print("Increase limit")
        break
    if(arr[number]):
        continue
    if(not testNum(number, primes)):
        break

print("The smallest odd composite number that cannot be written")
print("as a prime plus two times a square is %d" % (number))
print("Took %.3f seconds" % (time.time() - t))