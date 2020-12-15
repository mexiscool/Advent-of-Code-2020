
a =[int(i) for i in open('input.txt', 'r').read().split(',')]
#b = a*(int(2020/len(a)+1))
cnt = len(a)
dict = {}
for i,j in enumerate(a):
	dict[j] = i
last2 = a[-2]
last = a[-1]
while cnt <30000000:
	try:
		idx=dict[last]
		#print(last,idx, cnt, dict[0])
		last2, last = last, cnt-1-idx
		dict[last2] = cnt-1

	except:
		#print('ehm',last, last2)
		last2, last = last, 0
		dict[last2] = cnt-1
		
		

	cnt +=1
	if cnt%100000==0:
		print(cnt)
	#print(a[0:-1][::-1].index(j))
#print(a)

print(last)