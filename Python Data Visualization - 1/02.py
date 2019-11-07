import matplotlib.pyplot as pt
import numpy as np

with open('popu.txt', 'r') as fp:
	populations = fp.readlines()

print(populations)

city = []
popu = []

for p in range(len(populations)):
	if p > 10:
		cc, pp = populations[p].rstrip('\n').split(',')
		city.append(cc)
		popu.append(int(pp))

ind = np.arange(len(city))
print(ind)


print(city)
pt.bar(ind, popu)
pt.xticks(ind, city)
pt.title('Program 02')
pt.show()
