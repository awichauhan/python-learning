def forLoop():
    data = [2, 'Navin', 9, 10, 11]
    for i in data:  # cant pass the condition here; can use when we have list of values or collection of arrays
        print(i)
forLoop()


# using while loop
def readingValueOfList():
    data = [2, 'Navin', 9, 10, 11]
    n = len(data)
    i = 0
    while i < n:
        print(data[i])
        i += 1

readingValueOfList()