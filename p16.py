import time

start = time.time()

num = 2**1000
num = str(num)

total = 0
for x in num:
	total += int(x)

end = time.time() - start

print("\nThe sum of the digits of 2^1000 is %d\nTook %.3f seconds\n" % (total, end))