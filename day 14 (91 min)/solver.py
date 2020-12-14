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
		#print(str(bin(int(v[1]))[2:]).zfill(32)[::-1])
		for c, b in enumerate(str(bin(int(v[1]))[2:]).zfill(36)[::-1]):
			if j[0][-(c+1)] == 'X':
				temp.append(b)
			else:
				temp.append(j[0][-(c+1)])
		print(int("".join(temp)[::-1]))
		memory[int(v[0])] = int("".join(temp)[::-1],2)
print(sum(memory.values()))