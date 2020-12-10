a = [i for i in open('input.txt', 'r').readlines()]
passports = []
checks = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid = 0
temp = ''
for j in a:
	if j == '\n':
		k = temp.split()
		l = [m.split(':') for m in k]
		passport = {}
		for n in l:
			passport[n[0]]=n[1]
		passports.append(passport)
		temp = ''
	else:
		temp = temp + ' ' + j
		
def checker(passport):
	for check in checks:
		if check not in thing:
			return False
	return True
		
def deepchecker(passport):
	if not 1920 <=int(thing['byr'])<=2002:
		return False
	
	if not 2010 <=int(thing['iyr'])<=2020:
		return False
		
	if not 2020 <=int(thing['eyr'])<=2030:
		return False
		
	if thing['hgt'][-2:] == 'cm':
		if not 150 <= int(thing['hgt'].split('cm')[0]) <=193:
			return False
	elif thing['hgt'][-2:] == 'in':
		if not 59 <= int(thing['hgt'].split('in')[0]) <= 76:
			return False
	else:
		return False
		
	try:
		if len(thing['hcl'].split('#')[1]) != 6:
			return False
	except:
		return False
		
	if thing['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
		return False
	
	if len(thing['pid']) != 9:
		return False
		
	return True
		
for thing in passports:
	if checker(thing) and deepchecker(thing):
		print(thing['hgt'])
		valid += 1
		
print(valid)