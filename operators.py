def myOperators():

    # arithmetic operators
    a = 1
    b = 2
    c = a+b
    print(c)

    # a = a + 2
    a += 2  # assignment operator; short hand

    b = -b

    d = a-b   # binary operator
    e = a*b
    f = a/b
    g = a//b
    h = a % b

    x,y = 5,6

    print(d)
    print(e)
    print(f)
    print(g)
    print(h)

# relational operators

    i = a < b
    j = a <= b
    k = a >= b
    l = a == b
    m = a != b
    print(i)
    print(j)
    print(k)
    print(l)
    print(m)

# logical operators

    n = a < 10 and b >1  # truth table of AND operation (multiplication)
    o = a < 10 or b >1    # truth table of OR operation (addition)
    print(n)
    print(o)

    result = True
    print(not result)

myOperators()