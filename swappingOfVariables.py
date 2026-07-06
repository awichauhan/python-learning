def VariablesSwap():
    a = 5
    b = 6

    print("a: ", a)
    print("b: ", b)

#traditional way (extra variable)

    c = a
    a = b
    b = c

    print("a: ", a)
    print("b: ", b)
#another way (mathematical solution)

    a = a + b
    b = a - b
    a = a - b

    print("a: ", a)
    print("b: ", b)

# another way (python solution)

    a,b = b,a  # tuple packing  & tuple unpacking

    print("a: ", a)
    print("b: ", b)

VariablesSwap()