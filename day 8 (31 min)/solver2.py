b = open('input.txt', 'r').readlines()


for count,l in enumerate(b):
	accumulator = 0
	position = 0
	a = b.copy()
	if l.split()[0] == 'nop':
		a[count] = a[count].replace('nop','jmp')
	elif l.split()[0] == 'jmp':
		a[count] = a[count].replace('jmp', 'nop')
	#print(a)
	while True:
		if position == len(a):
			print('hit')
			__import__("sys").exit(str(accumulator))
		if a[position] == None:
			break
		j = a[position].split()
		if j[0] == 'nop':
			a[position] = None
			position += 1
			continue
		elif j[0] == 'acc':
			a[position] = None
			position+=1
			if j[1][0] == '+':
				accumulator += int(j[1][1:])
			else:
				accumulator -= int(j[1][1:])
			continue
		elif j[0] == 'jmp':
			a[position] = None
			if j[1][0] == '+':
				position += int(j[1][1:])
			else:
				position -= int(j[1][1:])
			continue
		print(position)

print('bad')