import math

sum = 0

def divisors(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


for i in range (1,999999999999999999999999):
    sum = sum + i
    if len(list(divisors(sum))) > 500:
        print(sum)
        quit()
