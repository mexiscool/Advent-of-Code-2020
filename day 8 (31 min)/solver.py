a = open('input.txt', 'r').readlines()

accumulator = 0
position = 0
while True:
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

print(accumulator)