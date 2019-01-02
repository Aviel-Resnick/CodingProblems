import math

nums = 0

def sumFunc(n):
    sumOfDivs = 0
    for i in range(1, math.ceil((n/2))+1):
        if n % i == 0:
            sumOfDivs += i
    return(sumOfDivs)

def test(a):
    b = sumFunc(a)
    if sumFunc(b) == a:
        return True
    else:
        return False

for i in range(1,10000):
    if test(i) == True:
        nums += i

print(nums)
#40285
