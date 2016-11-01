sumA = 0
sumB = 0

for i in range(1,101):
    val = i**2
    sumA = sumA + val
for x in range(1,101):
    sumB = sumB + x

square = sumB**2
result = square - sumA

print(result)
