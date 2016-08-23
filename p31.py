import time

t = time.time()

count = 1

# 100 cents
for a in range(2+1):
	# 50 cents
	for b in range(4+1):
		# 20 cents
		for c in range(10+1):
			#10 cents
			for d in range(20+1):
				# 5 cents
				for e in range(40+1):
					# 2 cents
					for f in range(100+1):
						# 1 cent
						for g in range(200+1):
							amount = 100*a + 50*b + 20*c + 10*d + 5*e + 2*f + g
							if(amount == 200):
								count += 1

t = time.time() - t

print("\nThe amount of ways to make 200 cents are %d\nTook %.3f seconds\n" % (count, t))