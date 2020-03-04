def kangaroo(x1, v1, x2, v2):
    #check if kangroo can catch first
    if x1 + v1 >  x2 + v2 and v1 > v2 :
        return('NO')
    else:
        kangOne = x1
        kangTwo = x2
        for i in range(10000) :
            if kangOne == kangTwo:
                return ('YES')   
            kangOne += v1
            kangTwo += v2
        return ('NO')    