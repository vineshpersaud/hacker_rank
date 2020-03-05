def getTotalX(a, b):
    counter = 0
    factors = 0
    while counter < 100:
        counter += 1
        if all(counter % num == 0 for num in a) and all(num % counter == 0 for num in b):
            factors +=1
    return (factors)

