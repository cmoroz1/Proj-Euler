import time

def lenOfCollatz(n):
	if(n == 1): return 1
	if(n%2 == 0):
		return 1 + lenOfCollatz(n/2)
	else:
		return 1 + lenOfCollatz(3*n + 1)

st = time.time()

maximum = 0
num = 0
for x in range(1, 1000001):
	l = lenOfCollatz(x)
	if(l > maximum): 
		maximum = l
		num = x

end = time.time()

print("\nThe number below 1,000,000 with the longest Collatz Chain is %d (chain \nlength %d)\nTook %.3f seconds\n" % (num, maximum, end-st))