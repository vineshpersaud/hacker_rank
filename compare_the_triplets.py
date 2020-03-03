def compareTriplets(a, b):
    c = 0 
    d = 0
    for i in range(3):
        if a[i] > b[i] :
            c += 1
        elif b[i] > a[i]:
            d+=1

    return('{}{}'.format(c,d))