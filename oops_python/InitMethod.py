class computer:

    # cpu = "i5"    # class variable

    def __init__(self, cpu, ram):    #CHECK HOW TO USE VARIABLE KEY LENGTH HERE   # THIS WILL BE CALLED EVERYTIME WE CALL THE FUNCTION BUT NOT A CONSTRUCTOR
        print("init called")
        # keyvar = "i5"    # local variable
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("i7, 16GB")

com1 = computer("i7", "20GB")
com2 = computer("i5", "16GB")
com1.config()
computer.config(com2)
print(com1.cpu)
print("config: ", com2.cpu)








