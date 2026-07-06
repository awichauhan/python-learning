def NestedIf():
    YourTDS = input("Enter the TDS value")

    YourTDS = int(YourTDS)

    if YourTDS <= 100:
        print("water is safe for drinking")

    if YourTDS > 100:
            if YourTDS <= 199:
                print("Potentially unsafe")
            else:
                print("Dangerous water")

def isWaterSafeForDrinking(tdsLevel):
    if tdsLevel <= 100:
        print("safe for drinking")
    elif tdsLevel < 200:
        print("potentially risky")
    else:
        print("risky water")


currentTdsLevel = int(input("Enter your current TDS level: "))
isWaterSafeForDrinking(currentTdsLevel)


