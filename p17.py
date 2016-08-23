import time

#
# Does not work for numbers with length 4
#
def numToWord(num):
	num = str(num)
	if(len(num) == 4):
		return "One thousand"
	if(len(num) == 3):
		if(num[1:3] == "00"):
			return numToWord(num[0]) + " hundred"
		else:
			return numToWord(num[0]) + " hundred and " + numToWord(num[1:3])
	if(len(num) == 2):
		if(num[1] == "0"):
			if(num == "10"): return "ten"
			if(num == "20"): return "twenty"
			if(num == "30"): return "thirty"
			if(num == "40"): return "forty"
			if(num == "50"): return "fifty"
			if(num == "60"): return "sixty"
			if(num == "70"): return "seventy"
			if(num == "80"): return "eighty"
			if(num == "90"): return "ninety"
		elif(num[0] == "0"):
			return numToWord(num[1])
		else:
			if(num == "11"): return "eleven"
			if(num == "12"): return "twelve"
			if(num == "13"): return "thirteen"
			if(num == "14"): return "fourteen"
			if(num == "15"): return "fifteen"
			if(num == "16"): return "sixteen"
			if(num == "17"): return "seventeen"
			if(num == "18"): return "eighteen"
			if(num == "19"): return "nineteen"
			return numToWord(num[0] + "0") + "-" + numToWord(num[1])
	if(len(num) == 1):
		if(num == "1"): return "one"
		if(num == "2"): return "two"
		if(num == "3"): return "three"
		if(num == "4"): return "four"
		if(num == "5"): return "five"
		if(num == "6"): return "six"
		if(num == "7"): return "seven"
		if(num == "8"): return "eight"
		if(num == "9"): return "nine"

s = time.time()

count = 0
for x in range(1, 1001):
	count += len(numToWord(x).replace(" ","").replace("-",""))

end = time.time() - s

print("\nThe sum of the letters of the numbers from 1 to 1000 is %d\nTook %.3f seconds\n" % (count, end))