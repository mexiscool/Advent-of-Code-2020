
a =[int(i) for i in open('input.txt', 'r').read().split(',')]
#b = a*(int(2020/len(a)+1))
cnt = len(a)
while cnt <2020:
	j = a[-1]
	try:
		t = a[0:-1][::-1].index(j)+1
		a.append(t)
	except:
		print('ehm')
		a.append(0)
	#print(a[0:-1][::-1])
	cnt +=1
	#print(a[0:-1][::-1].index(j))
print(a)
print(len(a))
print(a[-1])