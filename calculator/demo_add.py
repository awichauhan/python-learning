
import calculator
import calculator.addDemo as Demo

import addDemo # calling entire module
from math import floor #calling single function from module  (syntax: from module import function)

def newDemo():
    result = addDemo.addition(5,6)   #if imported entire module, need to call it as module.function
    op = floor(5.6)  # if function is imported already, then directly reference it
    print(op)
    print(result)

newDemo()

# terminal has to be changed to the required package path