def isPrime(num):
	for x in range(2, num//2+1):
		if(num%x == 0):
			return False
	return True

def primeFactors(num):
	pFactors = []
	for x in range(2, num//2):
		if(num%x==0 and isPrime(x)):
			pFactors.append(x)
			print(x)
	return pFactors

f = primeFactors(600851475143)

print("\nThe prime factors of 600851475143 are", f, "\nThe max prime factor is", max(f), "\n")