import time

size = 20

already_computed = {}

#
# Uses symmetry to only calculate half of the possible paths
# Make sure to multiply the result by 2
#
def numPaths(x, y, size):
	if(x == size and y == size):
		return 1
	if(x == size):
		return numPaths(x, y+1, size)
	if(y == size):
		return numPaths(x+1, y, size)
	if(x == 0 and y == 0):
		return numPaths(x+1, y, size)
	if(x == y):
		if((size-x) in list(already_computed.keys())):
			return already_computed[size-x]
	return numPaths(x+1, y, size) + numPaths(x, y+1, size)


for size in range(1, 21):
	start = time.time()
	ans = 2*numPaths(0, 0, size)
	already_computed[size] = ans
	elapsed_time = time.time() - start
	print("\nThe number of paths in a %d by %d grid is %d\nTook %.3f seconds\n" % (size, size, ans, elapsed_time))