from re import X


def evenGenerator(n):           # Question no :- 3
    x = 2
    while n:
        yield x 
        x += 2
        n -= 1
evenGenerator(5)
for e in evenGenerator(5):
    print(e,end = " ")