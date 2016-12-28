l = []
for i in range(2,11):
	x = float(1/i)
	l.append(x)

for x in range(0,len(l)):
	current = l[int(x)]
	for y in range(2,len(str(current))-2):
		print(str(current)[y])
	