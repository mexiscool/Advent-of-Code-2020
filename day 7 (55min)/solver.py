a = open('input.txt', 'r').readlines()
rules = {}
for i in a:
	rule = {}
	j = i.split('.\n')[0].split(' bags contain')
	#if j[0] == 'shiny gold':
	#	continue
	k = (j[1]).split(',')
	for m in k:
		n = m.split(' bag')[0]
		if n[3:] != ' other':
			rule[n[3:]] = int(n[1])
	rules[j[0]] = rule

def deepsearch(key):
	#print('key: '+str(key))
	for value in rules[key]:
		#print(value)
		if value == 'shiny gold':
			return True
		if deepsearch(value):
			return True
	return False
	
can_contain = 0
for key in rules:
	#print(key)
	if deepsearch(key):
		#print(key)
		can_contain += 1
print(can_contain)
	