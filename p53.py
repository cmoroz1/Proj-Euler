import time, math

t = time.time()

def combinations(n, r):
    return int(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))

count = 0
for n in range(1, 101):
    for r in range(1, n+1):
        if(combinations(n, r) > 1000000):
            count += 1

print("The number of nCr for n between 1 and 100 that are")
print("bigger than 1,000,000 are %d" % (count))
print("Took %.3f seconds" % (time.time() - t))