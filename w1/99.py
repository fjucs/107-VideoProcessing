
def main():
	for i in range(1, 10):
		for j in range(1, 10):
			print('{} * {} = {}'.format(i, j, i*j))
		print('')

	print('--------------------------------------------------------------------------', end='\n\n')

	for i in range(1, 10):
		for j in range(1, 10):
			print('{:1} * {:1} = {:2} '.format(i, j, i*j), end='')
		print()
	print('')

	print('--------------------------------------------------------------------------', end='\n\n')

	s = 1
	while s < 9:
		for i in range(1, 10):
			for j in range(3):
				print('{:1} * {:1} = {:2} '.format(s+j, i, (s+j)*i), end=' ')
			print('')
		print('')
		s += 3

	print('--------------------------------------------------------------------------', end='\n\n')

if __name__ == '__main__':
	main()