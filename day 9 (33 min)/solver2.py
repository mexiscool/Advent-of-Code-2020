a = [int(i) for i in open('input.txt', 'r').readlines()]
preamble = 25
sum_number = 530627549

def check(list):
	i = 0
	while True:
		if len(list)==i:
			#print('bad')
			return False
		if sum(list[0:i]) == sum_number:
			return i
		i+=1
	
for count,i in enumerate(a):
	if check(a[count:]):
		temp = check(a[count:])
		print(min(a[count:count+temp])+max(a[count:count+temp]))
		break
		
				
	