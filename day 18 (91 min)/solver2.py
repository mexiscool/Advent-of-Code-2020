a = [list(i) for i in open('input.txt', 'r').read().split('\n')]
def evaluate(i):
	#print(i)
	i = ''.join(i)
	i = i.split()
	while True:
		print('eval', i)
		try:
			idx = i.index('+')
			number = int(i[idx-1]) + int(i[idx+1])
			#print(idx+1)
			del i[idx-1:idx+2]
			i.insert(idx-1, number)
		except ValueError: 
			try:
				idx = i.index('*')
				number = int(i[idx-1]) * int(i[idx+1])
				del i[idx-1:idx+2]
				i.insert(idx-1, number)
			except ValueError: 
				break
	print('eval', i)
	return i[0]
	
def find(i):
	try:
		min = len(i)-i[::-1].index('(')
		max = min+i[min:].index(')')
		return False, min, max
	except:
		return True, 0, 0
	
sum = 0
for i in a:
	while True:
		bad, min,max = find(i)
		if bad:
			temp = evaluate(i)
			break
		temp = evaluate(i[min:max])
		del i[min-1:max+1]
		i.insert(min-1,str(temp))
		i.insert(min,' ')
		#print(min,max, temp)
		print(i)
	print(temp)
	sum += int(temp)
print(sum)
