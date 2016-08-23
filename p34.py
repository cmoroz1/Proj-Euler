import time
import math

t = time.time()

def factorialOfDigits(num):
	num = str(num)
	temp = 0
	for x in num:
		temp += math.factorial(int(x))
	return temp

lst = []

maximum = 10**6

for x in range(3, maximum):
	if(x == factorialOfDigits(x)):
		lst.append(x)

print("\nThe sum of the numbers which are equal to the sum of")
print("the factorial of their digits is %d" % (sum(lst)))

t = time.time() - t
print("Took %.3f seconds\n" % (t))