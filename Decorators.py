
def Deco(func):
    def wrap(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return wrap

@Deco
def deco_Subtraction(a,b):
    return a-b

@Deco
def divide(a,b):
    return a/b

result = divide(10,2)
print(result)

result2 = deco_Subtraction(10,5)
print(result2)