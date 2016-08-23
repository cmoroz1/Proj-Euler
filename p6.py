sumOfSq = 0
total = 0

for x in range(1, 101):
	sumOfSq += x**2
	total += x

sqOfSum = total**2

diff = sqOfSum - sumOfSq

print("\nThe difference between the square of the sum and the sum of the squares of the first 100 numbers is", diff, "\n")