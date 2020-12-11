import copy
a = open('input.txt', 'r').read().split('\n')
list = []
for i in a:
	list1 = []
	list1[:0] =i
	width = len(list1)
	list.append(list1)
height = len(list)
#print(list)
print(height,width)
def count(i,j):
	filled=0
	for l,k in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
		c=1
		while not (int(i+l*c) <0 or int(i+l*c) >= height or int(j+k*c) < 0 or int(j+k*c) >= width):
			#print(i+l*c,j+k*c)
			if list[i+l*c][j+k*c] == '.':
				c+=1
			elif list[i+l*c][j+k*c] == '#':
				filled+=1
				break
			elif list[i+l*c][j+k*c] == 'L':
				break
			else:
				print('ehm')
				break
	return filled

i=0
while True:
	list2 = copy.deepcopy(list)
	for m,val1 in enumerate(list):
		for n,val2 in enumerate(val1):
			if list[m][n] != '.':
				temp = count(m,n)
				if temp>=5:
					list2[m][n]='L'
				elif temp == 0:
					list2[m][n]='#'
	#print(list2)
	i+=1
	if list2 == list:
		break
	else:
		list = copy.deepcopy(list2)
counter = 0
for m,val1 in enumerate(list):
	for n,val2 in enumerate(val1):
		if val2 == '#':
			counter+=1
		
#print(list)
print(counter)
#print(i)	