import time

def factorial(n):
	p = 1
	for x in range(1, n+1):
		p *= x
	return p

t = time.time()

number = str(factorial(100))

total = 0
for x in number:
	total += int(x)

t = time.time() - t

print("\nThe sum of the digits of 100! is %d\nTook %.3f seconds\n" % (total, t))