import math
a = open('input.txt', 'r').readlines()
facing = 0
pos_x = 0
pos_y=0
rel_way_x = 10
rel_way_y= 1


for i in a:
	if i[0] == 'N':
		rel_way_y += int(i[1:])
	elif i[0] == 'E':
		rel_way_x += int(i[1:])
	elif i[0] == 'S':
		rel_way_y -= int(i[1:])
	elif i[0] == 'W':
		rel_way_x -= int(i[1:])
	elif i[0] == 'L':
		temp = math.atan2(rel_way_y,rel_way_x)
		temp = temp+math.radians(int(i[1:]))
		length = math.hypot(rel_way_x,rel_way_y)
		rel_way_x = (length*math.cos(temp))
		rel_way_y = (length*math.sin(temp))
	elif i[0] == 'R':
		temp = math.atan2(rel_way_y,rel_way_x)
		temp = temp+math.radians(-int(i[1:]))
		length = math.hypot(rel_way_x,rel_way_y)
		rel_way_x = (length*math.cos(temp))
		rel_way_y = (length*math.sin(temp))
	elif i[0] == 'F':
		pos_x += int(i[1:])*rel_way_x
		pos_y += int(i[1:])*rel_way_y
	#print(pos_x,pos_y)
	#print(rel_way_x,rel_way_y)
	#print()

print(int(abs(pos_x)+abs(pos_y)))