
import math   # module is bundle of many similar kind of functions

from math import sqrt  # restricting what functions can be imported from module

def myModule():
    num = 25
    result = sqrt(num)   #math.sqrt(num)
    print(result)

    ceil = math.floor(59.5)
    print(ceil)

myModule()

