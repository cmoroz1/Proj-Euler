import math

triples = []

for a in range(1, 750):
	for b in range(a, 750):
		c = math.sqrt(a*a + b*b)
		if(c == int(c)):
			triples.append((a, b, int(c)))

for trip in triples:
	if(trip[0] + trip[1] + trip[2] == 1000):
		print("\nThe pythagorean triples which add up to 1000 are %d, %d, %d\nTheir product is %d\n" % (trip[0], trip[1], trip[2], trip[0]*trip[1]*trip[2]))
		break
