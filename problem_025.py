def main():
	a = 1
	b = 1
	c = 0
	term = 2
	
	while (len(str(c)) < 1000):
		c = a + b
		a = b
		b = c
		term += 1
		
	print term

if __name__ == '__main__':
  main()