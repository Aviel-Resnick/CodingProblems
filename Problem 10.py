num = 2000000
isprimebool = True
prime_num = 0
sum = 0

def isprime(i,isprimebool, prime_num):
    for x in range(2,i-1):
        if i%x == 0:
            isprimebool = False
            return False
        
    if isprimebool == True:
        return True

for i in range (2, num):
        if isprime(i,isprimebool, prime_num) == True:
            print(i)
            sum = sum + i

print(sum)
