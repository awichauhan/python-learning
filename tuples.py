def myTuple():
    tup = [23,45,67,43]
    print(type(tup))
    tup = 23, 45, 67, 43
    print(type(tup))
    print(len(tup))
    tup1 = (2, 'navin', 7.9)
    print(tup1)
    num = tup1[2]
    print(num)
    num1, name, num2 = tup1  #unpacking the tuples into variables
   # num1, name, num2, num3 = tup1  #ValueError: not enough values to unpack (expected 4, got 3)
    print(num1)
    print(name)
    print(num2)
    tupB = (23, 'navin', [3,4,5,6])
    number1, name, list1 = tupB  # unpacking the list
    print(tupB[2])
    print(list1)
    tupB[2][:3] = [8,9,10,11]   # changing the list inside tuple
    # list1[:3] = [8,9,10,11]
    print(tupB)
    check1 = 8 in tupB[2]  #it wont check if we dont pass index number of list inside the tuple
    check2 = [8,9,10,11,6] in tupB
    check = 23 in tupB
    print(check1)
    print(check)
    print(check2)

myTuple()

# tuples are immutable