def fib_to(n):
    fibs = [0, 1]
    for i in range(2, n+1):
       fibs.append(fibs[-1] + fibs[-2])
    return fibs

for x in range (1,10000):
	l = fib_to(x)
	n = len(str(l[-1]))
	if n == 1000:
		print(x)
		break