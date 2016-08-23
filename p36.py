import time

t = time.time()

def toBinary(num):
    s = ""
    while (num > 0):
        rem = num % 2
        num = num // 2
        s += str(rem)
    return s[::-1]

def isPalindrome(num):
	return str(num) == str(num)[::-1]

lst = []
for x in range(1, 1000000):
	if(isPalindrome(x) and isPalindrome(toBinary(x))):
		lst.append(x)

t = time.time() - t

print("\nThe sum of all palindrome numbers in base 10 and 2")
print("is %d. Took %.3f seconds" % (sum(lst), t))

