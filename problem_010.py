def main():
	sum = 0
	lim = 2000000
	primes = []
	
	for i in range(lim):
		primes.append(1)
	
	for i in range(2, lim):
		if i*i < lim and primes[i] == 1:
			j = i
			while i*j < lim:
				primes[i*j] = 0
				j += 1
	
	for i in range(2, lim):
		if primes[i]:
			sum += i
	
	print(sum)
	
if __name__ == '__main__':
	main()
