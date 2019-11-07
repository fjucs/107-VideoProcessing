import matplotlib.pyplot as pt
import numpy as np

with open('popu.txt', 'r') as fp:
	populations = fp.readlines()

print(populations)

city = []
popu = []

for p in populations:
	cc, pp = p.rstrip('\n').split(',')
	city.append(cc)
	popu.append(int(pp))

ind = np.arange(5)
print(ind)

cnt = 0
p = [[],[],[],[]]
c = [[],[],[],[]]
print(p)
for i in range(0, 20, 5):
	for j in range(i, i+5):
		print(j)
		p[cnt].append(popu[j])
		c[cnt].append(city[j])

	pt.subplot(220 + cnt+1)
	pt.bar(ind, p[cnt])
	pt.xticks(ind, c[cnt])
	pt.title('city {}'.format(cnt+1))
	cnt += 1
pt.show()
