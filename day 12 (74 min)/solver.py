import math
a = open('input.txt', 'r').readlines()
facing = 0
pos_x = 0
pos_y=0

for i in a:
	#print(pos_x)
	#print(pos_y)
	if i[0] == 'N':
		pos_y += int(i[1:])
	elif i[0] == 'E':
		pos_x += int(i[1:])
	elif i[0] == 'S':
		pos_y -= int(i[1:])
	elif i[0] == 'W':
		pos_x -= int(i[1:])
	elif i[0] == 'L':
		facing -= int(i[1:])
	elif i[0] == 'R':
		facing += int(i[1:])
	elif i[0] == 'F':
		#print(pos_x)
		pos_x += int(i[1:])*math.cos(math.radians(facing))
		pos_y -= int(i[1:])*math.sin(math.radians(facing))

print(int(abs(pos_x)+abs(pos_y)))