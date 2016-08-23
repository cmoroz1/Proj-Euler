import time
import math

t = time.time()

def divisorPairs(num):
	pairs = {}
	for x in range(2, int(math.sqrt(num))+1):
		if(x*x == num):
			pairs[x] = x
		elif(num%x == 0):
			pairs[x] = int(num/x)
	return pairs

def containsNumbers(a, b, c):
	a = str(a)
	b = str(b)
	c = str(c)
	nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
	if(len(a) + len(b) + len(c) != 9):
		return False
	for x in a:
		if(x not in nums):
			return False
		else:
			nums.remove(x)
	for x in b:
		if(x not in nums):
			return False
		else:
			nums.remove(x)
	for x in c:
		if(x not in nums):
			return False
		else:
			nums.remove(x)
	return True

def isPandigital(num):
	pairs = divisorPairs(num)
	for n1, n2 in pairs.items():
		if(containsNumbers(n1, n2, num)):
			return True
	return False

lst = []

for x in range(10000):
	if(isPandigital(x)):
		lst.append(x)

print()
print("The sum of the products who can be written as pandigital is %d" % (sum(lst)))


t = time.time() - t
print("Took %f seconds\n" % (t))