class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self): #method overriding
        print("in B show")
    # pass

obj1 = B()
obj1.show()