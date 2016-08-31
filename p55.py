import time

t = time.time()

def reverseAdd(n):
    temp = str(n)
    return n + int(temp[::-1])

def isPalindrome(n):
    n = str(n)
    return n == n[::-1]

def isLychrelNum(n):
    count = 0
    while(count < 50):
        n = reverseAdd(n)
        if(isPalindrome(n)):
            return False
        count += 1
    return True

count = 0
for x in range(1, 10000+1):
    if(isLychrelNum(x)):
        count += 1

print("There are %d Lychrel numbers below 10,000" % (count))
print("Took %.3f seconds" % (time.time() - t))