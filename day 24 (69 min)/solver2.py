import numpy as np
a = open('input.txt', 'r').read().split('\n')
size = 100
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

def count(x,y):
	return sum([floor[y+1][x-1], floor[y+1][x], floor[y][x-1], floor[y][x+1], floor[y-1][x], floor[y-1][x+1]])
days = 100
floor2 = np.copy(floor)

for d in range(days):
	for y in range(2*size-2):
		y+=1
		for x in range(2*size-2):
			x+=1
			number = count(x,y)
			if floor[y][x] == 0 and number == 2:
				floor2[y][x] = 1
			elif floor[y][x] == 1 and (number == 0 or number > 2):
				floor2[y][x] = 0
	floor = np.copy(floor2)
	print(np.sum(floor))