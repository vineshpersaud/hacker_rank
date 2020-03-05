def birthday(s, d, m):
    pieces = 0
    total = []
    while len(s) >= m:
        for i in range (m):
            total.append(s[i])  
        if sum(total) == d and len(total) ==m :
           pieces +=1
        total = []
        s = s[1:] 
    return(pieces)