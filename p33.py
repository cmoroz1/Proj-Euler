import time
import math

t = time.time()

def findSameChars(a, b):
	lst = []
	for char in a:
		if(char in b and char not in lst):
			lst.append(char)
	return lst

def remove(string, char):
	temp = ""
	removed = False
	for x in string:
		if(x == char and not removed):
			removed = True
		else:
			temp += x
	return temp


class Fraction:
	def __init__(self, num, den):
		self.num = num
		self.den = den

	def simplify(self):
		gcd = math.gcd(self.num, self.den)
		if(gcd != 0):
			return Fraction(int(self.num/gcd), int(self.den/gcd))
		return Fraction(self.num, self.den)

	def canSimplifyWrong(self):
		num = str(self.num)
		den = str(self.den)
		same_char = findSameChars(num, den)
		if(len(same_char) == 0):
			return False
		for char in same_char:
			num = remove(num, char)
			den = remove(den, char)
		if(num == "0" or den == "0" or num == "" or den == ""):
			return False
		return True

	def simplifyWrong(self):
		num = str(self.num)
		den = str(self.den)
		same_char = findSameChars(num, den)
		for char in same_char:
			num = remove(num, char)
			den = remove(den, char)
		if(num == "0" or den == "0" or num == "" or den == ""):
			return Fraction(1, 1)
		return Fraction(int(num), int(den))

	def equals(self, other):
		self = self.simplify()
		other = other.simplify()
		return self.num == other.num and self.den == other.den

	def mult(self, other):
		num = self.num * other.num
		den = self.den * other.den
		return Fraction(num, den).simplify()

	def show(self):
		print("%d/%d" % (self.num, self.den))

lst = []

for den in range(2, 100):
	for num in range(1, den):
		if(num%10 == 0 or den%10 == 0):
			continue
		f = Fraction(num, den)
		if(f.canSimplifyWrong()):
			f1 = f.simplify()
			f2 = f.simplifyWrong()
			if(f1.equals(f2)):
				lst.append(f)

p = lst[0].mult(lst[1]).mult(lst[2]).mult(lst[3]).simplify()


t = time.time() - t

print("\n4 numbers which can be simplified both correctly and incorrectly\nare %d/%d, %d/%d, %d/%d, and %d/%d" % (lst[0].num, lst[0].den, lst[1].num, lst[1].den, \
																											lst[2].num, lst[2].den, lst[3].num, lst[3].den))
print("Their product in reduced terms is %d/%d" % (p.num, p.den))
print("Took %.3f seconds\n" % (t))