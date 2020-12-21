a = open('input.txt', 'r').read().split('\n')
#print(a)
ingredients = {}
foods = []
allergies = {}
for i in a:
	i, j = i.replace(')','').split(' (contains ')
	k = j.split(', ')
	j = list(k)
	i = i.split()
	
	for m in k:
		if m in allergies:
			allergies[m] +=1
		else:
			allergies[m] = 1
	
	for n in i:
		foods.append(n)
		try:
			for b in j:
				ingredients[n].append(b)
		except:
			ingredients[n] = []
			for b in j:
				ingredients[n].append(b)
			
allergenfree = []
#print(allergies)
#print(ingredients)
for key, value in ingredients.items():
	true = True
	for allergie in set(ingredients[key]):
		if not allergies[allergie] > value.count(allergie):
			true = False
	if true:
		allergenfree.append(key)
	
	
#print(counter)

#print(allergenfree)
sum = 0
for i in allergenfree:
	sum+=foods.count(i)
print(sum)

	