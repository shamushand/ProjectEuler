def main():
	sum = 1
	spiral = 3
	
	while spiral <= 1001:
		sum += 4 * spiral**2 - 6 * (spiral - 1)
		spiral += 2
		
	print(sum)

if __name__ == '__main__':
	main()
	input()	