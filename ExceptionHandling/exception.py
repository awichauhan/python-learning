

try:
    a = int(input("enter value of a: "))
    b = int(input("enter value of b: "))
    result = a/b
    print("result is: ", result)
except ZeroDivisionError as zde:
    print("An error occurred: Division by zero not allowed", zde)
except ValueError as ve:
    print("An error occurred: Invalid input. Please enter numeric values only", ve)
except Exception as e:  # storing the error in e and then printing it
    print("Unexpected error occurred.", e)
finally:
    print("resource closed")  #whatever happens perform the logic under finally block
print("End of execution")

