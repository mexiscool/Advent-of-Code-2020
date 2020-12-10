a = [int(i) for i in open('input.txt', 'r').readlines()]
#a = list(range(1,100))
difference = []
a.insert(0, 0)
a.insert(-1, max(a)+3)
a.sort(reverse=True)
#print(a)
c = a.pop(0)
while len(a)>0:
	i=0
	while i<len(a):
		if c-a[i]<4:
			i+=1
		else:
			break
	difference.append(i)
	c = a.pop(0)
difference.append(1)
print(difference)
str = ''.join(map(str, difference)).replace('33211','7').replace('3211','4').replace('211','2').replace('1','')
thingy = [int(b) for b in str]
#print(thingy)
product = 1
for x in thingy:
    product *= x
print(product)