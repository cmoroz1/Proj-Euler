def divisibleByRange(x, y):
	for num in range(2, y+1):
		if(x%num != 0):
			return False
	return True

found = False
num = 20

while(not found):
	if(divisibleByRange(num, 20)):
		break;
	else:
		num += 1

print("\nSmallest number divisible by 1 through 20 is", num, "\n")