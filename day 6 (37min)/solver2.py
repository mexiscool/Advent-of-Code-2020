a = open('input.txt', 'r').readlines()
groups = []
temp = []
for j in a:
	if j == '\n':
		groups.append(temp)
		temp = []
	else:
		temp.append(j.split('\n')[0])
		
results= []
for group in groups:
	results.append(set(group[0]).intersection(*group))
	
yesses = 0
for result in results:
	yesses += len(result)
	
print(yesses)