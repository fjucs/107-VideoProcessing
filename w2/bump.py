row = None
col = None
def main():
	with open('bump.txt', 'r') as f, open('bump_1.txt', 'w') as out:
		M = f.readlines()
		# print(M)
		row = [0] * len(M); col = [0] * len(M[0])
		total = 0
		# row
		for i in range(len(M)):
			row[i] = M[i].count('*')
			total += row[i]
		# col
		for i in range(len(M[0])):
			cnt = 0
			for j in range(len(M)):
				if M[j][i] == '*':
					cnt += 1
			col[i] = cnt

		print('{:3s} {:3s}'.format('Row', 'Col'))
		for i, j in zip(row, col):
			print('{:3d} {:3d}'.format(i, j))
		print('total = {}'.format(total))

		for i in range(len(M[0])):
			for j in range(len(M)-1, -1, -1):
				if M[j][i] != '\n':
					out.write(M[j][i])
			out.write('\n')


if __name__ == '__main__':
	main()