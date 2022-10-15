def endlessIterator():     #  Question no :- 7
    a,b = 0,1
    while True:
        yield a 
        a,b = b,a+b
it = endlessIterator()
list_1 = []
while True:
    ans = input("Do you wanna next term [y/n] ")
    if ans == "y":
        d = next(it)
        list_1.append(d)
    else:
        break
print(list_1)      