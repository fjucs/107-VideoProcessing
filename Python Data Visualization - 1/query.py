import os
import matplotlib.pyplot as pt
import numpy as np

name = []
data = []
running = True

def read():
	with open('climate.txt', 'r', encoding='utf-8') as f:
		dd = f.readlines()
		idx = 0
		for i in dd:
			ii = i.split('\t')
			# print(ii)
			name.append(ii[0])
			tmp = []
			for j in range(1, 14):
				tmp.append(float(ii[j]))
			data.append(tmp)
		idx += 1

msg = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def printMenu():
	cnt = 0
	for i in range(0, len(name), 5):
		for j in range(5):
			print('{:>2d} {:<3s}\t'.format(i+j+1, name[i+j]),end='')
		print()
		cnt += 1

def printGraph(i):
	idx = np.arange(12)
	print(idx)
	data[i].pop()
	print(data[i])
	pt.barh(idx, data[i])
	# pt.plot
	pt.yticks(idx, msg)
	pt.title(name[i])
	pt.show()


def menu():
	global running, pt
	
	printMenu()

	opt = int(input('Please input query >'))
	print()

	if opt == 0:
		running = False
		return
	opt -= 1

	printGraph(opt)

	# print('{} 1981-2010 Temperature'.format(name[opt]))
	# for i in msg:
	# 	print('{:>6s}'.format(i), end='')
	# print()
	# for i in range(0, 13):
	# 	print('{:>6s}'.format(data[opt][i]), end='')
	# print('\n')
	# pt = True

def main():
	pt.rcParams['font.sans-serif']=['simhei']
	read()
	while running:
		menu()

if __name__ == '__main__':
	main()
