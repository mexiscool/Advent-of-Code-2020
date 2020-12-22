players = open('input.txt', 'r').read().split('\n\n')
print(players)
dict = {}
for j,i in enumerate(players):
	i=i.split('\n')
	i = [int(k) for k in i[1:]]
	dict[j+1] = i
print(dict)
def run(deck1, deck2):
	previous1=[]
	previous2=[]
	while True:
		#print(deck1, deck2)
		w=0
		if deck1 in previous1 or deck2 in previous2:
			#print(deck1, previous1, deck2, previous2)
			return 1 , deck1, deck2
		if len(deck1) == 0:
			return 2, deck1, deck2
		elif len(deck2) == 0:
			return 1, deck1, deck2
		previous1.append(deck1.copy())
		previous2.append(deck2.copy())
		#print(dict)
		i= deck1.pop(0)
		j = deck2.pop(0)
		if len(deck1)>=i and len(deck2)>=j:
			w, _, _ = run(deck1[0:i], deck2[0:j])
		if w==1:
			deck1.append(i)
			deck1.append(j)
			continue
		elif w==2:
			deck2.append(j)
			deck2.append(i)
			continue
		if i>j:
			deck1.append(i)
			deck1.append(j)
		else:
			deck2.append(j)
			deck2.append(i)

i, dict[1], dict[2] = run(dict[1],dict[2])
result = 0
for j,k in enumerate(reversed(dict[i])):
	result+= (j+1)*k
print(result)	
