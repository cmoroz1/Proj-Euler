import time

t = time.time()

def findPrimeFactors(num, primes):
    factors = []
    index = 0
    while(num != 1):
        if(num%primes[index] == 0):
            factors.append(primes[index])
            while(num%primes[index] == 0):
                num /= primes[index]
        index += 1
    return factors

def testNumber(num, primes):
    l1 = findPrimeFactors(num, primes)
    if(len(l1) != 4):
        return False
    l2 = findPrimeFactors(num+1, primes)
    if(len(l2) != 4):
        return False
    l3 = findPrimeFactors(num+2, primes)
    if(len(l3) != 4):
        return False
    l4 = findPrimeFactors(num+3, primes)
    if(len(l4) != 4):
        return False
    return True

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

print("Testing numbers...")
number = 2*3*5*7
while(True):
    if(arr[number]):
        number += 1
        continue
    if(testNumber(number, primes)):
        break
    number += 1

print("The first number of the first four consecutive numbers")
print("to have four distinct factors is %d" % (number))
print("Took %.3f seconds" % (time.time() - t))