from re import A


def printFibonacci(n):                # Question no :- 5
    a,b = 0,1
    while n:
        yield a 
        a,b = b,a+b
        n -= 1
printFibonacci(15)
for e in printFibonacci(15):
    print(e,end = " ")       