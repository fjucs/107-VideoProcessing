import string

s = 'The International Conference on Digital Information Processing, Data Mining, and Wireless Communications'

ct = [0] * 26
def count(s):
	ss = s.lower()
	for i in ss:
		if i.isalpha():
			# print(ord(i)-ord('a'), i)
			ct[ord(i)-ord('a')] += 1
	cnt = 0
	for i in ct:
		if i > 0:
			cnt+= 1
	for i in s:
		if i.isupper():
			ct[ord(i)-ord('A')] -= 1
	return cnt

def main():
	print(count(s))

	for i in range(len(ct)):
		print('{} = {}'.format(chr(ord('a')+i), str(ct[i])))

	# dict
	dt = {}
	for i in string.ascii_letters:
		dt[i] = s.count(i)
	print(dt)



if __name__ == '__main__':
	main()