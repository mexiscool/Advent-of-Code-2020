import re
import random
import numpy as np
import itertools
import sys
np.set_printoptions(edgeitems=30, linewidth=100000)
a = open('input.txt', 'r').read().split('\n\n')
dict = {}
for j in a:
	j=j.split('\n')
	i = int(re.findall(r'\d+', j[0])[0])
	j = j[1:]
	j = [[1 if n == '#' else 0 for n in k] for k in j]
	j = np.array(j)
	dict[i] = [j, True]
#print(dict)
def rotate(i, times):
	if times == 0:
		return i
	return np.rot90(i,times)
	
def flip(i, axis):
	#0 up down
	#1 left rigth
	return np.flip(i, axis)
	
def checkseem(i,j, sideofi):
	#print(i,j)
	if sideofi == 0:
		i,j= i[0],j[-1]
	elif sideofi == 1:
		i,j = i[:,-1],j[:,0]
	elif sideofi == 2:
		i,j=i[-1],j[0]
	elif sideofi == 3:
		i,j=i[:,0],j[:,-1] #smh
	else:
		print('error check')
	#print(i,j)
	return	True if (np.array(i)==np.array(j)).all() else False
	
def checkaround(x,y,v, isokay):
	for t in (-1,0, 0),(0,1, 1),(1,0, 2),(0,-1, 3):
		try:
			if shape[y+v[0]+t[0]][x+v[1]+t[1]] != 0:
				if not checkseem(isokay, dict[shape[y+v[0]+t[0]][x+v[1]+t[1]]][0], t[2]):
					return False
		except IndexError:
			continue
	return True
	
	
def check(y,x,v):
	try:
		#print(shape[y+v[0]][x+v[1]])
		if shape[y+v[0]][x+v[1]] == 0:
			for p in dict:
				#print(dict[p][1])
				if dict[p][1]:
					for n in range(4):
						#print('test',dict[shape[y][x]][0], rotate(dict[p][0], n), v[2])
						#if checkseem(dict[shape[y][x]][0], rotate(dict[p][0], n), v[2]):
						if checkaround(x,y,v, rotate(dict[p][0], n)):
							#print('yay')
							shape[y+v[0]][x+v[1]] = p 
							dict[p] = [rotate(dict[p][0], n), False]
							return
						elif checkaround(x,y,v, rotate(flip(dict[p][0], 0), n)):
							shape[y+v[0]][x+v[1]] = p 
							dict[p] = [rotate(flip(dict[p][0], 0), n), False]
							return
				else:
					continue
	except IndexError:
		return

#print(dict[3079])
#print(flip(dict[3079],1))
#print(rotate(dict[3079],90))
#print(dict[1951], dict[2729])
#print(checkseem(dict[1951], dict[2729], 2))
size = np.sqrt(len(dict))
multivalid = []
for p in dict:
	#print(dict[p])
	counter = 0
	for d in dict:
		if p!=d:
			for v in range(4):
				for n in range(4):
					if checkseem(dict[p][0], rotate(dict[d][0], n), v):
						counter+=1
						#print(d,n,v)
					if checkseem(dict[p][0], rotate(flip(dict[d][0], 0), n), v):
						#print(d,n,v)
						counter+=1
	if counter <3:
		print(p,counter)
		multivalid.append(p)
product = 1
for i in multivalid:
	product*=i
print(product)
#print(rotate(flip(dict[2473][0], 0), 1))
exit()	
for q in multivalid:
	dict.pop(q, None)
		
print('step 2')
start_id, start_image = random.choice(list(dict.items()))
dict[start_id] = [start_image[0], False]
shape = np.zeros((int(2*size-1),int(2*size-1)))
shape[int(size-1)][int(size-1)] = start_id
print(shape)
while True:
	for y in range(int(2*size-1)):
		for x in range(int(2*size-1)):
			if shape[y][x] != 0:
				for v in ((-1,0, 0),(0,1, 1),(1,0, 2),(0,-1, 3)):
					check(y,x,v)
	print(shape)
	#print(dict)
	if sum([1 if h[1] else 0 for h in list(dict.values())]) == 0:
		break
print(shape)
		
