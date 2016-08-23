import time
import itertools
import math

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

def isPrime(num):
    for x in range(2, int(math.sqrt(num))+1):
        if(num%x == 0):
            return False
    return True

# print("\nGenerating primes...")
# limit = 999999999
# arr = [True]*limit
# arr[0] = arr[1] = False
# def sieve(x):
#     global arr, limit
#     for i in range(x*2, limit, x):
#         arr[i] = False
# sieve(2)
# for i in range(3, limit//2, 2):
#     sieve(i)
# primes = [i for i in range(2, limit) if arr[i]]

print("\nGenerating combinations of digits")
found = False
number = 0
digits = "987654321"
while(not found):
    lst = list(itertools.permutations(digits))
    lst.sort()
    print("Testing digits up to %d" % (len(digits)))
    for x in lst[::-1]:
        x = int("".join(x))
        if(isPrime(x)):
            found = True
            number = x
            break
    digits = digits[1:]

print("The largest pandigital prime number is %d" % (number))
print("Took %.3f seconds" % (time.time() - t))