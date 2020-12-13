a = open('input.txt', 'r').read().split('\n')
b = [int(i) for i in a[1].replace(',x','').split(',')]
#print(b)
c = b.copy()
while min(b)<int(a[0]):
	for j,k in enumerate(b):
		b[j] += c[j]
print(b)
print(c[b.index(min(b))]*(min(b)-int(a[0])))