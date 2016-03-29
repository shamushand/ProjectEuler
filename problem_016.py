def main():
	sum = 0
	value = str(2**1000)
	
	for i in range(0, len(value)):
		sum += int(value[i])
		
	print(sum)

if __name__ == '__main__':
	main()
