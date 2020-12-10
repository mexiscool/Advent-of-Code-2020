a = open('input.txt', 'r').readlines()
groups = []
temp = ''
for j in a:
	if j == '\n':
		groups.append(temp)
		temp = ''
	else:
		temp += j.split('\n')[0]
		
b= []
for group in groups:
	b.append(dict.fromkeys(group))

yesses = 0
for answers in b:
	yesses += len(answers)
	
print(yesses)