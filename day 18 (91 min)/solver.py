import re
a = [list(i) for i in open('input.txt', 'r').read().split('\n')]
def evaluate(i):
	next_op = ''
	number_left = None
	#print(i)
	i = ''.join(i)
	i = i.split()
	for j in i:
		if j == ' ':
			continue
		elif j == '+':
			next_op = '+'
		elif j == '*':
			next_op = '*'
		else:
			if next_op == '+' and number_left != None:
				number_left = number_left + int(j)
			elif  next_op == '*' and number_left != None:
				number_left = number_left * int(j)
			else:
				number_left = int(j)
	print('eval', i)
	return number_left
	
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