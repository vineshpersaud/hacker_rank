def plusMinus(arr):
    positiveCount = 0
    negativeCount = 0
    zeroCount = 0
    for num in arr :
        if num > 0 :
            positiveCount +=1
        elif num < 0:
            negativeCount +=1
        elif num == 0:
            zeroCount += 1

    print(format(positiveCount/len(arr), '.6f'))
    print (format(negativeCount/len(arr), '.6f'))
    print (format(zeroCount/len(arr), '.6f'))
