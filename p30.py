import time

t = time.time()

def fifthPowerDigits(num):
	num = str(num)
	total = 0
	for x in num:
		total += int(x)**5
	return total

maximum = 1000000

lst = []
for x in range(2, maximum):
	if(x == fifthPowerDigits(x)):
		lst.append(x)

count = len(lst)

t = time.time() - t

for x in range(len(lst)):
	lst[x] = str(lst[x])

print("\nThere are only %d numbers below %d which can be written as the sum\nof the fifth power of their digits\nThey are %s\nTook %.3f seconds\n" \
	% (count, maximum, ", ".join(lst), t))