import time

t = time.time()

#ALL COMBINATIONS OF a^b where a -> [2, 100], b -> [2, 100]
#HOW MANY UNIQUE COMBINATIONS

lst = []

for a in range(2, 100+1):
	for b in range(2, 100+1):
		result = a**b
		if(result not in lst):
			lst.append(result)

t = time.time() - t

print("\nThere are %d distinct terms for a^b where a and b are in [2, 100]\nTook %.3f seconds\n" % (len(lst), t))