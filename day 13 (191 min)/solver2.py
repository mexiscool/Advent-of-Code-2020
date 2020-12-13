from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
	
#copied above from rosetta code https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
	
a = open('input.txt', 'r').read().split('\n')
import math
b = a[1].split(',')
product = 1
n= []
a= []
for j,i in enumerate(b):
	if i !='x':
		n.append(int(i))
		a.append(int(j))
		product *=int(i)
		
print(product-chinese_remainder(n,a))