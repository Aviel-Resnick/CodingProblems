X_sum = 0

for i in range(1,1000):
    if i%5 == 0 or i%3 == 0:
        X_sum = X_sum + i
        print(i)

print (X_sum)
