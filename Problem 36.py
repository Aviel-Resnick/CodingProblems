import math

deciPalin = []
biPalin = []
final = 0

def checkPalin(i):
    a = str(i)
    b = a[::-1]

    if a == b:
        return True

def convert(x):
    counter = x
    binary = []
    while counter != 0:
        if counter % 2 == 0:
            binary.append(0)
        else:
            binary.append(1)
        counter = counter//2
    biInt = int(''.join(map(str,binary[::-1])))
    return(biInt)

def convertBack(x):
    num = int(str(x)[::-1])
    deci = 0

    for i in range(0, len(str(num))):
        val = str(num)[i] * (2**i)
        newVal = sum(map(int, str(val)))
        deci = deci + newVal

    return (deci)

for i in range(1,1000001):
    if checkPalin(i) == True:
        deciPalin.append(i)

for x in range(0,1998):
    if checkPalin(convert(deciPalin[x])) == True:
        biPalin.append(convert(deciPalin[x]))

for y in range(0, len(biPalin)):
    final = final + convertBack(biPalin[y])

print(final)
#872187
