# Slicing means taking a portion of a sequence

# syntax:  values[start : stop : step]

values = [10, 20, 30, 40, 50, 60]
print(values[1:5])  # Start from index 1, go up to index 5, but do not include index 5.



num = [x for x in range(1,11)]
print(num[2:10]) # starting from 2 but excluding 2
print(num[:5:-1]) # printing in reverse