import time

t = time.time()

# Implemented with recursion b/c why not
def isPandigital(num, test):
    num = str(num)
    test = str(test)
    if(len(num) == 0):
        return True
    if(test in num):
        num = num.replace(test, "")
        test = int(test) + 1
        return isPandigital(num, test)
    return False

print("\nGenerating primes...")
limit = 999999999
arr = [True]*limit
arr[0] = arr[1] = False
def sieve(x):
    global arr, limit
    for i in range(x*2, limit, x):
        arr[i] = False
sieve(2)
for i in range(3, limit//2, 2):
    sieve(i)
primes = [i for i in range(2, limit) if arr[i]]

print(primes[0:10])