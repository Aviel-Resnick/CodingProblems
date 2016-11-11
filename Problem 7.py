num = 999999999999999999999999999999999999999999999999999999999999999999
isprimebool = True
prime_num = 0

def isprime(i,isprimebool, prime_num):
    for x in range(2,i-1):
        if i%x == 0:
            isprimebool = False
            return False
        
    if isprimebool == True:

        return True

for i in range (2, num):
        if isprime(i,isprimebool, prime_num) == True:
            prime_num = prime_num + 1
            print(prime_num)
            if prime_num == 10001:
                print ("########", i)
                quit()
