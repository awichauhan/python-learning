from array import *
def arraysDemo():
    arr1 = array('i',[22,11,33,44,55])
    print(type(arr1.tolist()))
    print(arr1)

    print(arr1.buffer_info())  #memory address
    for value in arr1:
        print(value)

arraysDemo()