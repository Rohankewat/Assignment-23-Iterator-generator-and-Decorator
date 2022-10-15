def generatePrime():       # Question no :- 8
    a = 2     
    while True:
        yield a    
        a += 1     
it = generatePrime() 
l2 = []    
while True:
    ans = input("Do you want next prime number ")
    if ans == "y":
        d = next(it)
        if d == 2 or d == 3 or d == 5 or d==7 or d == 11 or d ==13:
            l2.append(d)   
        
        elif d%2!=0 and d%3 != 0 and d%5 != 0 and d%7 != 0 and d%11 != 0 and d%13 != 0:
            l2.append(d)
    else:
        break
print(l2)    