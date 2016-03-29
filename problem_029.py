def main():
	sum = 0
	
	for number in range(2, 500000):
		fsum = 0
		for ch in str(number):
			fsum += int(ch)**5
		if (fsum == number):
			sum += number
			
	print(sum)
if __name__ == '__main__':
	main()
	input()	