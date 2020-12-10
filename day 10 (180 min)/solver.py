a = [int(i) for i in open('input.txt', 'r').readlines()]
a.sort()
print(a)
b=0
difference = []
while len(a)>0:
	c = a.pop(0)
	difference.append(c-b)
	b=c
print(difference.count(1)*(difference.count(3)+1))
	