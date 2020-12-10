a = open('input.txt', 'r').readlines()
preamble = 25

def check(number, list):
	while True:
		if len(list) == 0:
			return False
		first = list.pop(0)
		for i in list:
			if int(first) + int(i) == number:
				return True
	return False
	
for count,i in enumerate(a[preamble:]):
	b = a[0+count:preamble+count].copy()
	#print(b)
	#print(i)
	if not check(int(i), b):
		print(i)

				
	