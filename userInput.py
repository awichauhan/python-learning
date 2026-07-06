def userInput():
    a = input("Enter value of a  ")  # input will be in string format
    b = input("Enter value of b ")

    d = input("Enter a character ")[0] # taking only first character

    a = int(a)   # need to convert it into integer type
    b = int(b)

    (a,b) = (b,a)
    c = a + b

    print("swapped a: ", a)
    print("swapped b: ", b)
    print("sum is ", c)
    print("value of d is ", d)

userInput()