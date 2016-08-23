import time

t = time.time()

limit = 10**6
print("\nCalculating primes...")
arr = [True]*limit
def sieve(x):
    global arr, limit
    for i in range(x*2, limit, x):
        arr[i] = False
for x in range(2, limit//2):
    sieve(x)
arr[0] = arr[1] = False
primes = [i for i in range(2, limit) if arr[i]]

def trun_left(num):
    num = str(num)
    for x in range(len(num)):
        curr = int(num[x:])
        if(not arr[curr]):
            return False
    return True


def trun_right(num):
    num = str(num)
    for x in range(1, len(num))[::-1]:
        curr = int(num[:x])
        if(not arr[curr]):
            return False
    return True

def trun(num):
    return trun_left(num) and trun_right(num)

print("Checking truncatable primes...")
lst = []
num = 11
for p in primes:
    if(p > 10 and trun(p)):
        lst.append(p)
    if(len(lst) == 11):
        break
print(lst)
print("Their sum is %d" % (sum(lst)))
print("Took %.3f seconds" % (time.time() - t))