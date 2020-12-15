a =[int(i) for i in open('input.txt', 'r').read().split(',')]
cnt = len(a)
dict = {}
for i,j in enumerate(a):
	dict[j] = i
last = a[-1]
while cnt <30000000:
	try:
		idx=dict[last]
		#print(last,idx, cnt, dict[0])
		dict[last] = cnt-1
		last = cnt-1-idx
	except:
		#print('ehm',last, last2)
		dict[last] = cnt-1
		last = 0
	cnt +=1
	#if cnt%100000==0:
	#	print(cnt)
	#print(a[0:-1][::-1].index(j))
print(last)