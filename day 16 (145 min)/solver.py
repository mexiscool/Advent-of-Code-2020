fields, mytick, othtick = open('input.txt', 'r').read().split('\n\n')
fields = fields.split('\n')
mytick = mytick.split('\n')[1]
othtick = othtick.split('\n')[1:]
dict = {}
for n in fields:
	i, j = n.split(': ')
	j, k = j.split(' or ')
	j,l = j.split('-')
	k,m = k.split('-')
	set1 = {*range(int(j),int(l)+1)}
	set2 = {*range(int(k),int(m)+1)}
	dict[i] = set1.union(set2)
adr = 0

def check(value):
	for field in dict:
		if dict[field].intersection({int(value)}) != set():
			return True
	return False
	
for tick in othtick:
	tick = tick.split(',')
	for value in tick:
		if not check(value):
			adr += int(value)
print(adr)