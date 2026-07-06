class A:
    def f1(self):
        print("f1 works")

    def f2(self):
        print("f2 works")

    def show(self):
        print("in A show")

class B:   # B is child class of class A (singe level inheritance)
    def f3(self):
        print("f1 works")
    def f4(self):
        print("f2 works")
    def show(self):
        print("in B show")

class C(A,B):   # class C(B): C is child class of class B (multi-level inheritance) But Class B doesnt have properties of Class C
    # class C(A,B): MULTILEVEL INHERITANCE follows Method Resolution Order (MRO)
    def f5(self):
        print("f1 works")
    def f6(self):
        print("f2 works")
    def show(self):
        print("in C show")

objectA = C()
objectA.f5()
objectA.show()
B.show(objectA)   # to specifically call the method of class B (although it is lower as per MRO)