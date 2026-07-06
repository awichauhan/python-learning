a = 5
b = 6
# c = a + b
c = int.__add__(a,b)

# because above data type is from class integer type, it is using the method add for this above operation. both + and __add__ is same (syntactic in backend)


a = 'awantika '
b = 'chauhan'
d = a + b

a = '5'
b = '6'
e = a + b

print(c.__str__())   # in backend this __str__ method is being used to just print the value of the variable (object) rather than the mem location
print(d)
print(e)

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):   # this is a built in method however, we can customize it: METHOD OVERRIDING
        return f'{self.name} : {self.balance}'

    def __add__(self,other):   # add operator overlaoding
        return Account('combined: ', self.balance + other.balance)

    def __gt__(self, other):   # greater than operator overloading
        return self.balance > other.balance


user1 = Account('awi', 4000)
user2 = Account('navin', 2000)
print(user1) # it will just print the memory location of user1 object without defining custom __str__ method in class Account
print(user2)

# combined = user1.balance + user2.balance
combined = user1 + user2
print(combined)


if user1 > user2:
    print("awi pays bill")
else:
    print("navin pays bill")

#operator overloading: one operator being used for different operations (POLYMORPHISM)