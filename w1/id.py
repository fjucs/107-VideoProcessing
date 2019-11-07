
cvt = {'A':10, 'B':11, 'C':12, 'D': 13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':34, 'J':18, 'K':19, 'L':20, 'M':21, 'N':22, 'O':35, 'P':23, 'Q':24, 'R':25, 'S':26, 'T':27, 'U':28, 'V':29, 'W':32, 'X':30, 'Y':31, 'Z':33}

def check(id):
	acc = cvt[id[0]] // 10 + cvt[id[0]] % 10 * 9
	# print(acc)
	for i in range(1, 9):
		# print("{} * {}".format(int(id[i]), 9-i))
		acc += int(id[i]) * (9-i)
	# print(acc)
	acc %= 10
	# print(acc)
	chk = 0 if acc == 0 else 10-acc
	# print(chk)

	if chk == int(id[9]):
		return True
	else:
		return False

def main():
	str_id = input('Enter your ID:')
	print(check(str_id))

if __name__ == "__main__":
	main()