import time

t = time.time()

def isPandigital(num):
    num = str(num)
    NUMBERS = ["1","2","3","4","5","6","7","8","9"]
    for x in num:
        if(x in NUMBERS):
            NUMBERS.remove(x)
        else:
            return False
    return len(NUMBERS) == 0

lst = []

for x in range(1, 9999):
    s = ""
    n = 1
    while(len(s) < 9):
        s += str(x*n)
        n += 1
    if(isPandigital(s)):
        lst.append(s)

print("\nThe largest pandigital number for Proj Euler #38 is %s" % (max(lst)))
print("Took %.3f seconds\n" % (time.time() - t))