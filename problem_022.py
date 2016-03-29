def main():
	sum = 0
	
	file = open('names.txt', 'r')
	names = file.read().split(',')
	names.sort()
	
	for name in names:
		score = 0
		temp = name.strip('"')
		for i in range(len(temp)):
			score += ord(temp[i]) - ord('A') + 1
		sum += score * (names.index(name) + 1)
	
	print(sum)

if __name__ == '__main__':
  main()
