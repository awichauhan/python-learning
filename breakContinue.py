def Continue():

    for i in range(10):
        if i % 3 == 0:  # for printing only numbers that are not divisible by 3
            continue # to stop when above condition meets and go back to starting condition
        print(i)

Continue()

def Break():

    for value in range(10):
        if value == 5:
            break  # to stop the loop and byee
        print(value)

Break()


