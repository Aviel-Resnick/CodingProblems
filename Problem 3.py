num = int(input("Input:"))
isprimebool = True

def isprime(i,isprimebool):
    for x in range(2,i-1):
        if i%x == 0:
            isprimebool = False
            
    if isprimebool == True:
        print (i)

for i in range (2, num):
    if num%i == 0:
        isprime(i,isprimebool)
