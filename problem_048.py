def main():
	sum = 0
	for i in range(1, 1000):
		sum += i**i
		
	print str(sum)[-10:]

if __name__ == '__main__':
  main()