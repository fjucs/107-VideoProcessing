
N = 10000
arr = [True] * (N+5)
prime = []

def era():
	arr[0] = arr[1] = False
	for i in range(2, N+1):
		if arr[i]:
			prime.append(i)
			for j in range(2*i, N+1, i):
				arr[j] = False

lower = 1
upper = 10

def main():
	era()
	cnt = 0
	for i in prime:
		if i >= lower and i <= upper:
			print(i, end=' ')

if __name__ == "__main__":
	main()