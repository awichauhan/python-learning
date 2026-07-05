def myVariable():
    a = 5
    b = 5
    c = 6

    print(id(a))  # printing memory address of variable a using inbuilt function "id"
    print(id(b))  # same address as variable a as they both having same value
    print(id(c))

    name = 'awantika'
    myname = 'awantika'  # STRING INTERNING: using same object for two variables
    print(id(name))
    print(id(myname))

    d = 'my fav my color is black'
    e = 'my fav my color is black'

    print(id(d))
    print(id(e))

    f = 1000000
    g = 1000000

    print(id(f))
    print(id(g))

myVariable()

# a,b are referring to same object (storing value 5); to utilize memory
# everything in python is object
# garbage collection will clear the unused object