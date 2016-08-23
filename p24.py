import time
import itertools

t = time.time()

p = list(map("".join, itertools.permutations("0123456789")))

p.sort()

t = time.time() - t

print("\nThe millionth permutation of 0123456789 is %s\nTook %.3f seconds\n" % (p[1000000 - 1], t))