
#class and static methods

class computer:

    brand = "Apple"  # class variable

    def __init__(self,cpu, ram, ssd):
        # self, cpu, ram, ssd are local parameters
        self.cpu = cpu
        # self.cpu = instance variable
        # cpu = local parameter
        self.ram = ram
        self.ssd = ssd

    def config(self): # instance method for logic related to each particular object of this class
        # self is a local parameter
        print("config is: ", self.cpu, self.ram, self.ssd)

    def info(self):
        return computer.brand
    # class variable to be used inside instance method

    @classmethod  # class method is used for logic related to the class/shared data.
    def brandinfo(cls):  #cls is a reference to the class, just as self is a reference to an object.
        return cls.brand
    # class variable used inside a class method

#class variable goes to class namespace and instance variable goes to instance namespace
    @staticmethod
    def gb_to_bytes(gb):
        return gb * (1024 ** 3)

com1 = computer("i5", "16GB","2TB")
print(com1.config())
print(com1.brand)  #we can directly access class variable
print(computer.brandinfo()) # but accessing it via a method (function) we need to have variable "brand" defined under class method
print(com1.brandinfo())
print(com1.gb_to_bytes(16))


