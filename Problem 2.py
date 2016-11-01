a = 1
b = 1
s = 0

while True:
    c = a + b
    a = b
    b = c
    if a > 4000000:
        print("DONE:", s)
        break
    else:
        print(a)
        if a%2 == 0:
            s = s + a
