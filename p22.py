import time

def letterSum(s):
	total = 0
	s = s.upper()
	for x in s:
		total += ord(x) - ord('A') + 1
	return total

t = time.time()

f = open("names.txt", "r")
names = f.read()
f.close()
names = names.replace('"', '')
names = names.split(",")
names.sort()

total = 0

for i in range(len(names)):
	total += (i+1)*letterSum(names[i])

t = time.time() - t

print("\nThe sum of the name scores in names.txt is %d\nTook %.3f seconds\n" % (total, t))