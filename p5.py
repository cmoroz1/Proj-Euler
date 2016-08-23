import time

t = time.time()

def divisibleByRange(x, y):
	for num in range(2, y+1):
		if(x%num != 0):
			return False
	return True

found = False
num = 1*2*3*5*7*11*13*17*19*2 # Makes number divisible by primes and 20

while(not found):
	if(divisibleByRange(num, 20)):
		break;
	else:
		num += 20

print("\nSmallest number divisible by 1 through 20 is", num, "\n")
print("Took %.3f seconds" % (time.time() - t))