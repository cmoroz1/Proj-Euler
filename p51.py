import time, math

t = time.time()

print("Calculating primes...")
limit = 1000000
arr = [True]*limit
arr[0] = arr[1] = False
def sieve(x):
    global arr, limit
    for i in range(x*2, limit, x):
        arr[i] = False
for x in range(2, int(math.sqrt(limit))+1):
    sieve(x)
primes = [i for i in range(2, limit) if arr[i]]

def replace(word, index, char):
    word = str(word)
    temp = list(word)
    temp[index] = char
    word = "".join(temp)
    return word

def familyOfEight(num, c):
    count = 0
    for char in "0123456789":
        temp = str(num).replace(c, char)
        if(int(temp) > 100000 and arr[int(temp)]):
            count += 1
    return count == 8

print("Testing primes...")
for p in primes:
    if(p > 100000):
        p = str(p)
        last_digit = p[-1:]
        if(p.count("0") == 3 and familyOfEight(p, "0") or \
           p.count("1") == 3 and last_digit != 1 and familyOfEight(p, "1") or \
           p.count("2") == 3 and familyOfEight(p, "2")):
            print("The first prime which has a family of 8 is %s" % (p))
            break

print("Took %.3f seconds" % (time.time() - t))