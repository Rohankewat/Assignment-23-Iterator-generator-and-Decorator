def deco_Triangle(printPerimeter):          # Question no :- 9
    def typeOfTriangle(a,b,c):
        if a == b == c:
            print("Equilateral triangle")
        elif a == b != c or a != b == c or a == c != b:
            print("Isosceles triangle")
        else:
            print("neither equilateral nor isosceles triangle")
        printPerimeter(a,b,c)
    return typeOfTriangle 
@deco_Triangle    
def printPerimeter(a,b,c):
    print("Perimeter of triangle is",a+b+c)
printPerimeter(10,5,10)    