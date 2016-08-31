import time

t = time.time()

def digitSum(num):
    total = 0
    for x in str(num):
        total += int(x)
    return total

print("Testing numbers...")
maximum = 0
for a in range(1, 100):
    for b in range(1, 100):
        n = digitSum(a**b)
        if(n > maximum):
            maximum = int(n)
print("The maximum digit sum of a^b, a,b < 100, is %d" % (maximum))
print("Took %.3f seconds" % (time.time() - t))