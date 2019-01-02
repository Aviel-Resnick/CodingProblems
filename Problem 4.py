def ispalindrome(val,i,x):
    a = str(val)
    b = a[::-1]

    if a == b and int(a) > 99999 and i < 1000 and x < 1000:
        print (a)

for i in range(1,1000):
    for x in range(1,1000):
        val = i * x
        ispalindrome(val,i,x)
