def generatePrime(a):       # Question no :- 6
    a = 2
    while True:
        yield a    
        a += 1
it = generatePrime(25) 
l2 = []    
n = 25
while n:
    d = next(it)
    if d == 2 or d == 3 or d == 5 or d==7 or d == 11 or d ==13:
        l2.append(d)   
        n -= 1
    elif d%2!=0 and d%3 != 0 and d%5 != 0 and d%7 != 0 and d%11 != 0 and d%13 != 0:
        l2.append(d)
        n -= 1
print(l2)    