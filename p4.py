def isPalindrome(num):
	num = str(num)
	return num == num[::-1]


largest =  0

for x in range(100, 999):
	for y in range(100, 999):
		if(x*y > largest and isPalindrome(x*y)):
			largest=x*y

print("\nThe largest palindrome from multiplying two 3 digit numbers is", largest, "\n")