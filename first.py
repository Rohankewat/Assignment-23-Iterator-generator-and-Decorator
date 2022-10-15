def printSet(s1):         # Question no :- 1
   it = iter(s1)
   count = 0
   while len(s1) != count:
      print(next(it),end = " ")
      count += 1

printSet({1,5,2,3,11,14})     