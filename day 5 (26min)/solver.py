a = [[i[0:7],i[7:10]] for i in open('input.txt', 'r').readlines()]
ids = []
spots = []
for j in a:
	rows = list(range(128))
	cols = list(range(8))
	for k in j[0]:
		if k == 'F':
			rows = rows[:int(len(rows)/2)]
		else:
			rows = rows[int(len(rows)/2):]
			
	for k in j[1]:
		if k == 'L':
			cols = cols[:int(len(cols)/2)]
		else:
			cols = cols[int(len(cols)/2):]
		#print(cols)
	#print('row: '+str(rows))
	#print('cols: '+str(cols))
	spots.append((rows[0],cols[0]))
	ids.append(8*rows[0] + cols[0])

import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
b = np.zeros((128,8))
for spot in spots:
	b[spot[0],spot[1]]=1
print(b[70:90])
#solution was 70*8+2=562
print(max(ids))