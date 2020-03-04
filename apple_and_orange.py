def countApplesAndOranges(s, t, a, b, apples, oranges):
    yardFruitCount = {"apples": 0,"oranges" :0}

    for apple in apples:
        appleLocation = a + apple
        if appleLocation >= s and appleLocation <= t:
            yardFruitCount['apples'] +=1
    
    for orange in oranges:
        orangeLocation= b+orange
        if orangeLocation >= s and orangeLocation <= t:
            yardFruitCount['oranges'] +=1


    print (yardFruitCount['apples'])
    print (yardFruitCount['oranges'])