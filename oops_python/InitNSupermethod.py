class A:   # every class in python is a child class ; and it inherits from parent class "OBJECT"

    def __init__(self):   #it will be called by child class if not __init__ is not defined in child class
        print("in A init")
    def f1(self):
        print("f1 works")

class B(A):
    def __init__(self):   # if this is not defined, it will go to A class
        super().__init__()   #object of super class A and call its __init__ function
        print("in B init")
    def f1(self):
        print("f1 works")

obj1 = B()
obj1.f1()
