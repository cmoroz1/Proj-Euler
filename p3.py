def isPrime(num):
	for x in range(2, num//2+1):
		if(num%x == 0):
			return False
	return True

def primeFactors(num):
	pFactors = []
	test = 2
	while(num != 1):
		if(num % test == 0):
			num = num//test
			while(num % test == 0):
				num = num//test
			pFactors.append(test)
		test += 1
	return pFactors



f = primeFactors(600851475143)

print("\nThe prime factors of 600851475143 are", f, "\nThe max prime factor is", max(f), "\n")