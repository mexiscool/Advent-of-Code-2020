players = open('input.txt', 'r').read().split('\n\n')
print(players)
dict = {}
for j,i in enumerate(players):
	i=i.split('\n')
	i = [int(k) for k in i[1:]]
	dict[j+1] = i
print(dict)
def run():
	while True:
		if len(dict[1]) == 0:
			return 2
		elif len(dict[2]) == 0:
			return 1
		#print(dict)
		i= dict[1].pop(0)
		j = dict[2].pop(0)
		if i>j:
			dict[1].append(i)
			dict[1].append(j)
		else:
			dict[2].append(j)
			dict[2].append(i)

i = run()
result = 0
for j,k in enumerate(reversed(dict[i])):
	result+= (j+1)*k
print(result)	
