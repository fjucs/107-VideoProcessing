
N = 30

def fibo_square(i):
	if i == 0:
		return 0
	elif i == 1:
		return 1
	else:
		return fibo_square(i-1) + fibo_square(i-2)

# def fibo_linear(i):
	

def main():
	print(fibo_square(N))

if __name__ == "__main__":
	main()