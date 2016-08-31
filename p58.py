import time, math
t = time.time()

# print("Generating primes...")
# limit = 1000000000
# arr = [True]*limit
# arr[0] = arr[1] = False
# def sieve(x):
#     global arr, limit
#     for i in range(x*2, limit, x):
#         arr[i] = False
# for x in range(2, math.ceil(math.sqrt(limit))+1):
#     sieve(x)
# primes = [i for i in range(2, limit) if arr[i]]

primes = {}
primes[1] = False
primes[2] = True

def isPrime(n):
    global primes
    try:
        return primes[n]
    except KeyError:
        if(n%2 == 0):
            primes[n] = False
            return False
        for x in range(3, math.ceil(math.sqrt(n))+1, 2):
            if(n%x == 0):
                primes[n] = False
                return False
        primes[n] = True
        return True

def checkDiagonals(size):
    lst = [1]
    count = 1
    increment = 2
    times = 4
    while(count < size*size):
        count += increment
        lst.append(count)
        times -= 1
        if(times == 0):
            increment += 2
            times = 4
    n_primes = 0
    for x in lst:
        if(isPrime(x)):
            n_primes += 1
    return (n_primes/(2*size-1))*100

print("Testing spirals...")
percentage = 100
count = 3
while(percentage > 10):
    count += 2
    percentage = checkDiagonals(count)

print("The first spiral which has less than 10 percent primes")
print("on the diagonals has a side length of %d" % (count))
print("Took %.3f seconds" % (time.time() - t))