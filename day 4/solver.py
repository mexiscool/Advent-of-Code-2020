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
		print(passports[-1])
		temp = ''
	else:
		temp = temp + ' ' + j
		
def checker(passport):
	for check in checks:
		if check not in thing:
			return False
	return True

for thing in passports:
	if checker(thing):
		valid += 1
		
print(valid)