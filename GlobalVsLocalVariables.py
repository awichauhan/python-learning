
a = 15    # GLOBAL VARIABLE
def globalLocalVarDemo():
    # a = 10   #LOCAL VARIABLE: DEFINED UNDER THE FUNCTION

    globals()['a']   # just importing a variable
    # (globals())  # importing all global variables
    a = 10  # can change it inside function
    print("inside a: ", a)

globalLocalVarDemo()
print("outside a: ", a )