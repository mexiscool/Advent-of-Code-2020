import numpy as np
a = open('input.txt', 'r').read().split('\n')
size = 40
floor = np.zeros((2*size, 2*size))
coords = []
print(floor)
for i in a: 
	x = size
	y = size
	i = list(i)
	while True:
		if len(i)==0:
			break
		j = i.pop(0)
		if j == 'e':
			x+=1
		elif j== 'w':
			x-=1
		else:
			k = i.pop(0)
			if j+k == 'se':
				y-=1
				x+=1
			elif j+k == 'sw':
				y-=1
			elif j+k == 'nw':
				y+=1
				x-=1
			elif j+k == 'ne':
				y+=1
	floor[y][x] = not floor[y][x]
	coords.append((x,y))
print(coords)
print(np.sum(floor))