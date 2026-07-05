def mySet():  #collection of unique elements; collection of values; collection of unordered elements
    set1 ={23,56,78,32,56}
    print(set1)  # output: {56, 32, 78, 23}
    check = 23 in set1
    print(check)
    print(type(set1)) # output: <class 'set'>
    set2 = {}
    print(type(set2))  # output: <class 'dict'>
    set2 = set()
    print(type(set2))  # output: <class 'set'>

    set3 = set('abcdefgh')
    set4 = set('aeioupd')
    print(set3)
    print(set4)
    print(set3 - set4)
    print(set3 | set4) #intersection
    print(set3 & set4) #union
    print(set3 ^ set4) #uncommon
    tup = (45)
    print(type(tup))
    tup = (45,)
    print(type(tup))

mySet()

#take the value (num or string) and perform hashing and then give u the hash value; speeds the process of fetching
