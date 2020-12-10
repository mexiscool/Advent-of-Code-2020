a=[__import__('re').split('-| |: |\n', i)[0:4] for i in open('input.txt', 'r').readlines()]
k=0
for j in a:
	if (j[3][int(j[0])-1]==j[2]) ^ (j[3][int(j[1])-1]==j[2]):
		k+=1
print(k)