import time

t = time.time()

def isRightTriangle(a, b, c):
    return a**2 + b**2 == c**2

def findPossibleTriangles(p):
    lst = []
    for a in range(1, p//2):
        for b in range(1, p//2):
            c = p - a - b
            if(isRightTriangle(a, b, c)):
                if(c not in lst):
                    lst.append(c)
    return len(lst)

maximum = 0
num = 0

print("\nCalculating different perimeters...")
for p in range(10, 1000+1):
    temp = findPossibleTriangles(p)
    if(temp > maximum):
        maximum = temp
        num = p

print("The maximum number of solutions is %d for a perimeter of %d" % (maximum, num))
print("Took %.3f seconds\n" % (time.time() - t))