max = 1000
x = 1
lst = []
while x < max:
	if (x % 3 == 0):
		lst.append(x)
	elif (x % 5 == 0):
		lst.append(x)
	x += 1

sum = 0
for num in lst:
	sum = sum + num

print("\n\nThe sum of all multiples of 3 or 5 below 1000 is", sum, "\n\n")