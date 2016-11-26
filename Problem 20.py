product = 1
sum = 0
for i in range (-100,-1):
	num = abs(i)
	product = product * num

str_factorial = str(product)
for x in range(0,len(str_factorial)):
	sum = sum + int(str_factorial[x])
print(sum)