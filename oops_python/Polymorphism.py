#if a bird quacks like a duck, it is a duck
# if a crow quacks like a duck, it is a duck

class Laptop:
    def build(self):
        print("laptop builds")
class Desktop:
    def build(self):
        print("desktop builds")
class Developers:
    def code(self, machine = Laptop()):  # cant call build function directly so need to create an object of Laptop class
        # machine = Laptop()  could have done this way but passed it as parameter
        print("Developers build")
        machine.build()
class Tablet:
    def open_pdf(self):
        print("opening PDF")

asus_rog = Laptop()
LG = Desktop()
Awantika = Developers()
Lenovo = Tablet()

# Awantika.code(asus_rog)
# Awantika.code(LG)
Awantika.code(Lenovo)  # this does not work because tablet does not have build function


# even if we have passed the object of Laptop class to Developer class and imported the method (identical to class Desktop and Laptop) within the method of class Developer.  But passed
# the object of class Desktop while calling the function of class Developer, it will use the method of class Desktop.