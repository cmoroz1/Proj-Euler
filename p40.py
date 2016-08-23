import time

t = time.time()

def createNumber(l):
    length = 0
    num = 1
    s = ""
    while(length < l):
        s += str(num)
        length += len(str(num))
        num += 1
    return s

print("\nCreating number...")
n = createNumber(10**6)

print("Finding digits...")
lst = []
product = 1
for index in [10**y for y in range(7)]:
    lst.append(int(n[index-1:index]))
    product *= int(n[index-1:index])
print("Digits are: ", end="")
print(lst)

print("The product of the digits is %d" % (product))
print("Took %.3f seconds" % (time.time() - t))