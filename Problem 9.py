ixy = []

for i in range (0,1000):
    for x in range (0,1000):
        for y in range (0,1000):
            if i + x + y == 1000:
                if i**2 + x**2 == y**2:
                    print(i*x*y)
                    exit()
