import time

t = time.time()

def generateTriangleNumbers(num):
    lst = []
    count = 1
    val = (count*(count+1))//2
    while(val <= num):
        lst.append(val)
        count += 1
        val = (count*(count+1))//2
    return lst

def wordVal(word):
    total = 0
    for char in word:
        total += ord(char) - ord('A') + 1
    return total

def isTriangleNum(n):
    global lst
    return n in lst

def isTriangleWord(word):
    return isTriangleNum(wordVal(word))

print("Generating triangle numbers...")
lst = generateTriangleNumbers(500)

print("Opening, reading, and formatting file...")
f = open("words.txt", "r")
words = f.read()
f.close()

words = words.replace("\"", "")
words = words.split(",")

print("Checking for triangle words...")
count = 0
for word in words:
    if(isTriangleWord(word)):
        count += 1

print("There are %d triangle words in \"words.txt\"" % (count))
print("Took %.3f seconds" % (time.time() - t))