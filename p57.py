import time
from fractions import gcd
t = time.time()

class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        return

    def invert(self):
        return Fraction(self.den, self.num)

    def __repr__(self):
        return "{}/{}".format(self.num, self.den)

    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def reduce(self):
        c = gcd(self.num, self.den)
        return Fraction(self.num//c, self.den//c)

    def add(self, num):
        if(isinstance(num, Fraction)):
            return Fraction()
        return Fraction(num*self.den + self.num, self.den)

def sqrt2Expansion(k):
    if(k == 1):
        return Fraction(3, 2)
    else:
        temp = Fraction(2, 1)
        for n in range(1, k):
            temp = temp.invert().add(2)
        return temp.invert().add(1)

print("Calculating the expansions of sqrt(2)...")
count = 0
for x in range(1, 1001):
    temp = sqrt2Expansion(x)
    if(len(str(temp.num)) > len(str(temp.den))):
        count += 1
print("There are %d fractions in the 1,000 expansions which have" % (count))
print("a larger numerator than denominator")
print("Took %.3f seconds" % (time.time() - t))