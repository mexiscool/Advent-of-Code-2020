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
	print('key: '+str(key))
	sum = 1
	for value in rules[key]:
		print(value)
		sum += deepsearch(value)*rules[key][value]
	return sum

print(deepsearch('shiny gold') - 1)	