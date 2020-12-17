import numpy as np
import sys
import itertools
np.set_printoptions(threshold=sys.maxsize)
a = open('input.txt', 'r').read().split('\n')
z0 = [list(i) for i in a]
width = len(z0[0])
size = 24
array = np.zeros((size, size, size-1))
for i,y in enumerate(z0):
	for j,x in enumerate(y):
		if x == '#':
			array[round(size/2-width/2+j)][round(size/2-width/2+i)][round((size/2-1))] = 1

offsets	= list(itertools.product([-1,0,1], repeat=3))
def neighbors(x,y,z):
	adr = 0
	for i in offsets:
		if i != (0,0,0):
			try:
				adr += array[x+i[0]][y+i[1]][z+i[2]]
			except:
				continue
	return adr
	
array_copy = np.copy(array)
print(np.sum(array))
iterations = 6
for l in range(iterations):
	array = array_copy.copy()
	for z in range(size-1):
		for y in range(size):
			for x in range(size):
				neigh = neighbors(x,y,z)
				if array[x][y][z] == 1:
					if not 2 <= neigh <= 3:
						array_copy[x][y][z] = 0
				elif array[x][y][z] == 0:
					if neigh == 3:
						array_copy[x][y][z] = 1
print(np.sum(array_copy))
