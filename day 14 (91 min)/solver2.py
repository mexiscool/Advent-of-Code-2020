import itertools
a = open('input.txt', 'r').read().split('mask = ')
#print(a)
memory = {}
for i in a[1:]:
	j = i.split('\nmem[')
	#print(j)
	k = [k.split('\n') for k in j[1:]]
	#print(k)
	m = [l[0].split('] = ') for l in k]
	#print(m)
	
	for v in m:
		temp = []
		counter = 0
		#print(str(bin(int(v[1]))[2:]).zfill(32)[::-1])
		for c, b in enumerate(str(bin(int(v[0]))[2:]).zfill(36)[::-1]):
			if j[0][-(c+1)] == 'X':
				temp.append('X')
				counter +=1
			elif j[0][-(c+1)] == '1':
				temp.append('1')
			elif j[0][-(c+1)] == '0':
				temp.append(b)
		#print(int("".join(temp)[::-1]))
		for u in itertools.product([0,1], repeat=counter):
			temp2 = temp.copy()
			for o in u:
				temp2 = ''.join(temp2).replace('X', str(o), 1)
			#print(temp2)
			memory[int(temp2[::-1],2)] = int(v[1])
print(sum(memory.values()))