import time, math

t = time.time()

def pentagonalNum(n):
    return (n*(3*n-1))//2

def isPentagonalNum(n):
    if(n <= 0):
        return False
    x = (1+math.sqrt(1+24*n))/6
    return int(x) == x

print("Generating pentagonal numbers...")
lst = []
for x in range(1, 3001):
    lst.append(pentagonalNum(x))

print("Checking numbers...")
for x in range(len(lst)):
    for y in range(x):
        if(isPentagonalNum(lst[x]-lst[y]) and isPentagonalNum(lst[x]+lst[y])):
            print("The two pentagonal numbers are %d and %d" % (lst[x], lst[y]))
            print("Their sum is %d and their difference is %d" % (lst[x]+lst[y], lst[x]-lst[y]))
            break

print("Took %.3f seconds" % (time.time() - t))