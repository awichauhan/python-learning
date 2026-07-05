def myString():
    name = 'Awantika'
    job = "Awantika's Job"
    job1 = 'Awantika\'s "Job"'  #cancelling the affect of special character using \ backward slash #
    HelloString = 'Hello ' * 10  #math operation with strings
    Fullname = 'Awantika ' 'Chauhan'  #python literals 'Awantika'
    AnotherName = 'Mona ' + 'Chauhan' #concatenation
    ShortName = Fullname[:8]  # or [0:8]
    NickName = AnotherName[0:]
    Text = "I am learning \n Python" #new line
    text2 = """
    I am learning 
    Python second time
    in my life
    """

    print(name)
    print(job)
    print(job1)
    print(HelloString)
    print(Fullname)
    print(AnotherName)
    print(Fullname[0]) #python list
    print(Fullname[-1]) #python assigns negative index for the same string to be read in reverse order
    print(ShortName)
    print(NickName)
    print(len(job))
    print(Text)
    print(text2)

myString()

