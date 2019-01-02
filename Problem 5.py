for i in range (1,9999999999):
    isdivis = True
    for x in range (1,21):
        if i%x != 0:
            isdivis = False

    if isdivis == True:
        print (i)
