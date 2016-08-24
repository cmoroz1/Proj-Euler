import time, math

t = time.time()

def quadratic(a, b, c):
    x_1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    x_2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    return [x_1, x_2]

def isTriangleNum(x):
    num = quadratic(1, 1, -2*x)[0]
    return int(num) == num

def isPentagonalNum(x):
    num = quadratic(3, -1, -2*x)[0]
    return int(num) == num

def isHexagonalNum(x):
    num = quadratic(2, -1, -x)[0]
    return int(num) == num


print("Starting with 40755...")
print("Testing numbers...")
number = 40755
index = 285
found = False
while(not found):
    index += 1
    number += index
    if(isHexagonalNum(number) and isPentagonalNum(number) and isTriangleNum(number)):
        found = True

print("The next number, after 40755 that is a triangle number,")
print("a pentagonal number, and a hexagonal number is %d" % (number))
print("Took %.3f seconds" % (time.time() - t))