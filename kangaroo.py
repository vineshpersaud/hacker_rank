def kangaroo(x1, v1, x2, v2):

    if x1 + v1 >  x2 + v2 and v1 > v2 :
        return('NO')
    else:
        kangOne = x1
        kangTwo = x2
        for i in range(1000) :
            kangOne += v1
            kangTwo += v2
            if kangOne == kangTwo:
                return ('YES')   
            if i == 999:
                return ('NO')    