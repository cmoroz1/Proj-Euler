import time

t = time.time()

def arePermutations(a, b, c):
    a = str(a)
    b = str(b)
    c = str(c)
    for char in a:
        if(char not in b or char not in c):
            return False
    for char in b:
        if(char not in a or char not in c):
            return False
    for char in c:
        if(char not in a or char not in b):
            return False
    return True

print("Calculating primes...")
limit = 10000
arr = [True]*limit
def sieve(x):
    global limit, arr
    for x in range(x*2, limit, x):
        arr[x] = False
for x in range(2, limit//2):
    sieve(x)
primes = [i for i in range(2, limit) if arr[i]]
print("Getting all 4 digit primes...")
four_digit_primes = [x for x in primes if len(str(x)) == 4]

print("Testing the 4 digit primes...")
numbers = []
for i in range(len(four_digit_primes)):
    if(four_digit_primes[i] == 1487):
        continue
    for j in range(i+1, len(four_digit_primes)):
        diff = four_digit_primes[j] - four_digit_primes[i]
        test = four_digit_primes[j] + diff
        if(test in four_digit_primes):
            if(arePermutations(four_digit_primes[i], four_digit_primes[j], test)):
                numbers = [four_digit_primes[i], four_digit_primes[j], test]
                break
    if(len(numbers) == 3):
        break

print("The three prime numbers which are a common distance apart")
print("and which are permutations of one another are:")
print(numbers)
print("Took %.3f seconds" % (time.time() - t))