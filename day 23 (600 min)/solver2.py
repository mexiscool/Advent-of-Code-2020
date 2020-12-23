a = [int(k) for k in '523764819']
a+=list(range(10,1000000+1))
b = len(a)
current_cup = (0, a[0])
destination_cup = ()
def move():
	global a, current_cup, threecups, destination_cup
	threecups = []
	threecups_idx = []
	for indx in range(current_cup[0]+1, current_cup[0]+4):
		threecups.append(a[indx%b])
		threecups_idx.append(indx%b)
	threecups_idx.sort(reverse=True)
	if threecups_idx[0]==threecups_idx[1]+1==threecups_idx[1]+1==threecups_idx[2]+2:
		del a[threecups_idx[2]:threecups_idx[0]+1]
		#print('ee')
	else:
		for n in threecups_idx:
			del a[n]

	i = 1
	while True:
		if current_cup[1]-i in threecups:
			i+=1
			#print(i)
			#print(i,a,current_cup[1]-1)
		elif current_cup[1]-i<1:
			i = current_cup[1]-b
		else:
			#print(i, current_cup[1]-i)
			destination_cup = (a.index(current_cup[1]-i), current_cup[1]-i)
			break
	for indx, el in enumerate(threecups):
		a.insert((destination_cup[0]+indx+1)%b, el)
	#print(a)
	#count = 0
	#for u in threecups_idx:
	#	if u<current_cup[0]:
	#		count+=1
	#get slower further in, a[destination_cup[0]+1:destination_cup[0]+1] =threecups
	c = a.index(current_cup[1])+1 # this index search is calculatable
	if c>b-1:
		c=c-b
	#print(c)
	#print(a)
	current_cup = (c, a[c])
	
for j in range(10000000):
	#print('Move: ', j+1)
	#print(current_cup, a)
	move()
	#print(threecups, destination_cup)
	if j%1000==0:
		print(j/10000000*100, '%')
		print(len(a), current_cup, destination_cup, threecups)
	
print('Final')
#print(current_cup, a)
print(a[a.index(1):4])
#assert a == [5, 8, 3, 7, 4, 1, 9, 2, 6]

