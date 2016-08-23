def fibUpTo(max):
	lst = []
	lst.append(1)
	lst.append(2)
	current = 2
	nextNum = lst[current-1] + lst[current-2]
	while(nextNum < max):
		lst.append(nextNum)
		current+=1
		nextNum = lst[current-1] + lst[current-2]
	return lst

lst = fibUpTo(4000000)
sum = 0

for x in lst:
	if(x%2 == 0):
		sum += x

print("\nThe sum of even Fibonacci numbers up to 4,000,000 is", sum, "\n")