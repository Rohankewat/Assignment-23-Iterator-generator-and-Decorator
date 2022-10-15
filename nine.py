def decorator_coprime(calculateHcf):   # Question no :- 10
    def coprimeOrNot(a,b):
        if a>b:
            large = a              
        else:
            large = b                   
        while True:
            if a % large == 0 and b % large == 0:
                if large == 1:
                    print("numbers are co-prime")
                    break
                else:
                    print("numbers are not co-prime")
                    break
            large -= 1
    
        calculateHcf(a,b)
    return coprimeOrNot
@decorator_coprime              
def calculateHcf(a,b):
    if a>b:
        large = a
    else:
        large = b
    while True:
        if a % large == 0 and b % large == 0:
            print("Hcf of",a,"and",b,"is",large)
            break
        
        large -= 1
calculateHcf(8,15)