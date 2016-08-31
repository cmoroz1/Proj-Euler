import time
t = time.time()

def xor(int1, int2):
    return int(int1) ^ int(int2)

def runDecription(text, test):
    temp = text.copy()
    for index in range(len(text)):
        count = index % len(test)
        temp[index] = xor(text[index], test[count])
    return temp

def convertToStr(text):
    s = ""
    for x in text:
        s += chr(x)
    return s

f = open("cipher.txt", "r")
text = f.read()
f.close()
text = text.split(",")

# ord('a') = 97, ord('z') = 122
found = False
for a in range(97, 123):
    for b in range(97, 123):
        for c in range(97, 123):
            test = [a, b, c]
            decripted_text = convertToStr(runDecription(text, test))
            if("the" in decripted_text and "and" in decripted_text and "I" in decripted_text and "have" in decripted_text):
                found = True
                break
        if(found):
            break
    if(found):
        break

total = 0
for x in decripted_text:
    total += ord(x)

print("The decription key is \"%s%s%s\"" % (chr(test[0]), chr(test[1]), chr(test[2])))
print("The sum of the ASCII values is %d" % (total))
print("Took %.3f seconds" % (time.time() - t))