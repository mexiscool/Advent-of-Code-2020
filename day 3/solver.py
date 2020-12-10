a = [i for i in open('input.txt', 'r').readlines()]
trees_list = []
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
width = len(a[0])
height = len(a)
for j in slopes:
	trees = 0
	x, y = (0,0)
	while True:
		x += j[0]
		x %= width-1
		y += j[1]
		if y > height-1:
			break;
		if a[y][x] == '#':
			trees += 1
	trees_list.append(trees)
print(trees_list)
print(__import__('math').prod(trees_list))
