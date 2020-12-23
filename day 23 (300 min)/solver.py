a = [int(k) for k in '523764819']	
b = len(a)
threecups = []
current_cup = (0, a[0])
destination_cup = ()
def move():
	global a, current_cup, threecups, destination_cup
	threecups = []
	for indx in range(current_cup[0]+1, current_cup[0]+4):
		threecups.append(a[indx%b])
	for n in threecups:
		del a[a.index(n)]
	#print(a)
		
	#threecups = a[current_cup[0]+1:current_cup[0]+4]
	#del a[current_cup[0]+1:current_cup[0]+4]
	i = 1
	while True:
		if a.count(current_cup[1]-i) == 0:
			i+=1
			if current_cup[1]-i<1:
				i = -b
			#print(i,a,current_cup[1]-1)
		else:
			destination_cup = (a.index(current_cup[1]-i), current_cup[1]-i)
			break
	for indx, el in enumerate(threecups):
		a.insert((destination_cup[0]+indx+1)%b, el)
	#print(a)
	#a = a[0:destination_cup[0]+1] + threecups + a[destination_cup[0]+1:]
	c = a.index(current_cup[1])+1
	if c>b-1:
		c=c-b
	#print(c)
	#print(a)
	current_cup = (c, a[c])
	
for j in range(100):
	print('Move: ', j+1)
	print(current_cup, a)
	move()
	print(threecups, destination_cup)
	
print('Final')
print(current_cup, a)

