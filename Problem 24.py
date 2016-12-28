import itertools

numbers = [0,1,2,3,4,5,6,7,8,9]

a = list(itertools.permutations(numbers, 10))
d = []

for i in range(0,len(a)):
	b = a[i]
	c = ''.join(str(e) for e in b)
	d.append(c)

print(d[999999])