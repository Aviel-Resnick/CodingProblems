longest = 0

for i in range (1,1000000):
    num = i
    currentLen = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            currentLen = currentLen + 1
        else:
            num = num * 3 + 1
            currentLen = currentLen + 1

    #print (i)
    if currentLen > longest:
        longest = currentLen
        print ("Longest:", i)
