def dataTypes():
    x = 10
    print(type(x))

    pi = 3.14
    print(type(pi))

    c = 6 + 8j
    print(type(c))

    a = 2
    b = 3
    d = complex(a,b)
    print(d)

    k = int(pi)  # type convertor
    print(k)
    print(type(k))

    p = float(k)
    print(p)
    print(type(p))

    is_it = False
    print(is_it)

    q = int(is_it)
    print(q)

    blank = None # none data type
    print(blank)

    r = range(10)
    print(r)
    print(type(r))

    set(r)
    print(set(r))

    l = set(range(2,11,2))
    print(l)

dataTypes()