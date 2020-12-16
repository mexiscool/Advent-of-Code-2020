fields, mytick, othtick = open('input.txt', 'r').read().split('\n\n')
fields = fields.split('\n')
mytick = mytick.split('\n')[1].split(',')
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
	
def loop(tick):
	for value in tick:
		if not check(value):
			return False
	return True
			
	
validtick = []
for tick in othtick:
	tick = tick.split(',')
	if loop(tick):
		validtick.append(tick)
		
result = []
for x in range(len(validtick[0])):
	options = []
	temp = list(list(zip(*validtick))[x])
	temp = [{int(i)} for i in temp]
	#print(temp)
	
	for i, item in enumerate(temp):
		options2 = set()
		for field in dict:
			if dict[field].intersection(item) != set():
				options2 = options2.union({field})
		options.append(options2)
	result.append(options[0].intersection(*options[1:]))
#print(result)
result2 = list(''.zfill(len(fields)))
while True:
	
	#print(result)
	for j,i in enumerate(result):
		if len(i) == 1:
			temp = result[j]
			result[j] = set()
			result2[j] = [str(s) for s in temp][0]
			break
	breaky =True
	for i in result:
		if i != set():
			breaky = False
	if breaky:
		break
	for i in range(len(result)):
		result[i] = result[i] - temp
print(result2)
prod = 1
#print(mytick)
for j,i in enumerate(result2):
	if i.startswith('departure'):
		prod*=int(mytick[j])
print(prod)
