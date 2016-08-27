import time

t = time.time()

def p52(num):
    digits = list(str(num))
    for x in range(2, 7):
        for char in str(num*x):
            if(char not in digits):
                return False
    return True

number = 0
while(True):
    number += 1
    if(len(str(number)) == len(str(6*number)) and p52(number)):
        break

print("The smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x")
print("all contain the same digits is %d" % (number))
print("Took %.3f seconds" % (time.time() - t))