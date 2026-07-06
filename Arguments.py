def add(num1, num2 ):  # not defining type of parameters
    print(type(num2))   # this will print based on what type of argument we passed in function call
    return num1 + num2

result = add('awi','chauhan')    #it can take integer type or string type argument
print(result)

def sub(num3,num4 = 0):  # DEFAULT ARGUMENT already passed
    return num3 - num4

result2 = sub(3)
print(result2)

def multiply(num5, *num6):  #VARIABLE LENGTH ARGUMENT to accept second argument as tuple
    print(num5)
    print(num6)
    product = num5
    for n in num6:
        product = product * n
    return product

result3 = multiply(1,2,3,4)
print(result3)

def person(name, age=18):  # default argument to be accepted if no argument is provided
    print("name: ", name)
    print("age: ", age)

person('Navin',89) # if argument is provided then accept it

person(age = 40, name = 'Awantika')  # KEYWORD ARGUMENT

def newPerson(name, **vararguments):  #KEYLENGTH ARUGUMENT
    print(vararguments) # printing entire dictionary
    for n,m in vararguments.items():
        print(n, ": ", m)

newPerson(name = 'Awantika', age = 40, location = "Delhi",)