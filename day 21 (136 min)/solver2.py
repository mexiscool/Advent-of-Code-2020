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

for key, value in ingredients.items():
	true = True
	for allergie in set(ingredients[key]):
		if not allergies[allergie] > value.count(allergie):
			true = False
	if true:
		allergenfree.append(key)
	
for i in allergenfree:
	ingredients.pop(i,None)
	
allegen = []
mathchingredient = {}
#print(ingredients)
while True:
	#print(ingredients)

	for key, value in ingredients.copy().items():
		for allergie, count in allergies.items():
			if value.count(allergie)<count or count == 0:
				ingredients[key] = list(filter((allergie).__ne__, ingredients[key]))
		#print(ingredients)
		if len(set(ingredients[key])) == 1:
			allegen.append(ingredients[key][0])
			mathchingredient[allegen[-1]]=key
			allergies[ingredients[key][0]] = 0
			ingredients.pop(key, None)
			break
		#print(allergies)
	if len(ingredients) == 0:
		break
allegen.sort()
str=''
for i in allegen:
	str+=mathchingredient[i]+','
print(str[:-1])

	