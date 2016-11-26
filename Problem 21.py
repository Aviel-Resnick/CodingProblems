l = []

def d(n):
	sumx = 0
	for i in range(1,n+1):
		if n % i == 0 and i < n:
			sumx = sumx + i
	return sumx

def test(num):
	num1 = d(num)
	num2 = d(num1)

	if num2 == num and num2 != num1:
		l.append(num)
		l.append(num1)

for x in range(200,10000):
	test(x)
print(sum(list(set(l))))