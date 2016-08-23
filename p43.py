import time, itertools

t = time.time()

def isPandigital(num):
    num = str(num)
    numbers = "0123456789"
    for char in num:
        if(char in numbers):
            numbers = numbers.replace(char, "")
        else:
            return False
    return len(numbers) == 0

def p43Divisible(num):
    num = str(num)
    return int(num[1:4])%2 == 0 and int(num[2:5])%3 == 0 and int(num[3:6])%5 == 0 and int(num[4:7])%7 == 0 and int(num[5:8])%11 == 0 and int(num[6:9])%13 == 0 and int(num[7:10])%17 == 0

print("Generating combinations of 0-9...")
lst = list(itertools.permutations("0123456789"))

print("Calculating total of pandigital & p43divisible numbers...")
total = 0
for x in lst:
    x = int("".join(x))
    if(p43Divisible(x) and isPandigital(x)):
        total += x

print("The total is %d" % (total))
print("Took %.3f seconds" % (time.time() - t))