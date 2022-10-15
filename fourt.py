def printSquares(n):            # Question no :- 4
    x = 1
    while n:
        yield x**2
        x += 1
        n -= 1
printSquares(10)    
for e in printSquares(10):   
    print(e,end = " ")   