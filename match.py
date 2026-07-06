def matchDemo():

    waterTDS = input("Enter the TDS value: ")
    waterTDS = int(waterTDS)

    match waterTDS:

        case _ if waterTDS < 100:
            print("Water is safe")

        case _ if waterTDS > 100 and waterTDS <= 199:  # cant use &, have to use and, or
            print("Water has potential risk")

        case _:
            print("Water is dangerous to drink")

matchDemo()