import itertools

def main():
	counter = 0
	foo = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
	
	bar = itertools.permutations(foo)
	
	for i in bar:
		counter += 1
		
	print counter
	
if __name__ == '__main__':
	main()