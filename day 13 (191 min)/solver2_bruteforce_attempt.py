a = open('input.txt', 'r').read().split('\n')
import math
b = a[1].split(',')
#print(b)
c = b.copy()
t=100000000000000
b=[]
stateorigin=0
for j,i in enumerate(c):
	if i != 'x':
		b.append(round(round(t/int(i))*int(i)))
		stateorigin += 1
	else:
		b.append('x')
print(stateorigin)
print(b)
while True:
	state = 0
	for j,k in enumerate(b):
		if k!='x':
			if t+j==int(k):
				state+=1
			else:
				continue
	if state==stateorigin:
		break
	#if t >= 5000 :
	#	print(t,state,b)
	#	break
	b[0] = int(b[0])+ int(c[0])
	t=int(b[0])
	for j,k in enumerate(b[1:]):
		if k!='x':
			while t+j+1>int(b[j+1]):
				b[j+1] = int(b[j+1])+ int(c[j+1])
	#min = b[0]
	#for j in b[1:]:
	#	if j != 'x':
	#		if int(j)<min:
	#			min=int(j)


	#print(b,state)
print(t)