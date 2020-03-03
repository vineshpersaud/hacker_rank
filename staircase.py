def staircase(n):
    spaces = n-1
    for i in range(n):
        print(" "*spaces + "#"*(n-spaces))
        spaces -= 1