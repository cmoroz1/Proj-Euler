import time

fib_dict = {1:1, 2:1}

def fib(n):
	if(n in list(fib_dict.keys())):
		return fib_dict[n]
	result = fib(n-1) + fib(n-2)
	fib_dict[n] = result
	return result

t = time.time()

length = 0
count = 0
while(length != 1000):
	count += 1
	length = len(str(fib(count)))

t = time.time() - t

print("\nThe index of the first Fibonacci number to contain 1000 digits is %d\nTook %.3f seconds\n" % (count, t))