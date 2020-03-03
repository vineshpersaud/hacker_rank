def diagonalDifference(arr):

    # sum of each diagonal
    diagonalLeft = 0
    diagonalRight = 0

    # count of index left and right
    leftLoop = 0
    rightLoop = -1

    for row in arr:
        diagonalLeft += row[leftLoop]
        diagonalRight += row[rightLoop]
        leftLoop +=1
        rightLoop -= 1

        #abs to return postive
    return abs(diagonalLeft-diagonalRight)