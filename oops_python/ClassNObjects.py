# object: have some properties and behaviors
# class is a blueprint; you design an object in class; it will have properties and methods

class Calculator:                      # new class
    a = 10                             # variable of the class
    def add(x,y):                      # method of a class (when u define a function inside a class, it is method)
        sum = x + y
        return sum
    def name(self):   #self restricts to define for which object of this class, i m calling this function; x = Calculator.name(newObject), where newObject is one object of class Calculator
        print("Name of calculator is My Calc")
        return
class Calculator_object:             #  different class
    newAssignmentClass = Calculator           #assigning a class to another variable
    newObject = Calculator()                 # creating an object (instantiation of the class)
    print(type(newObject))                  # now newObject is of class type '__main__.Calculator'


    summation = Calculator.add(4,5)  # object is a instantiation of the class & passing parameters to the method

    Calculator.name(newObject)  # had to define newObject as self has been passed as parameter in function "name"; to represent current object
    newObject.name()      #this way also newObject is being passed as parameter to method name
    print(Calculator.a)
    print(summation)
    print(type(summation))  #object of class type 'int'


