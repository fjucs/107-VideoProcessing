import random, os

def main():
	random.seed('I\'m a random seed')

	cnt = 0
	guess = int(random.randint(1, 100))
	while True:
		cnt += 1
		n = int(input('Please input a number: '))
		if n > guess:
			print('Your number is greater than the secret number')
		elif n < guess:
			print('Your number is lesser than the secret number')
		else:
			print('Congrat!')
			print('You have guessed {} times'.format(cnt))
			break
		print()

if __name__ == "__main__":
	main()