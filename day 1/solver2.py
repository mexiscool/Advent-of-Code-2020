a=[int(i) for i in open('expenses-report.txt', 'r').readlines()]
while (True): 
	k = a.pop(0)
	for l in a:
		for m in a:
			if l + k + m == 2020:
				__import__("sys").exit(str(l*k*m))
