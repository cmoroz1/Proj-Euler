import time

t = time.time()

total = 0
for n in range(1, 1001):
    total += n**n
total = str(total)
last_ten = total[len(total)-10:len(total)]
print("The last ten digits of 1^1 + 2^2 + ... + 1000^1000 are %s" % (last_ten))
print("Took %.3f seconds" % (time.time() - t))