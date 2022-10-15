def oddGenerator(n):         # Question no :- 2
    x = 1
    while n:
        yield x
        x += 2
        n -= 1
oddGenerator(10)
for e in oddGenerator(10):
    print(e,end = " ")   