a=[int(i) for i in open('expenses-report.txt', 'r').readlines()]; exec('while (True): k = a.pop(0); [__import__("sys").exit(str(l*k)) if (l + k == 2020) else False for l in a]')
