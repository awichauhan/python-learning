# a concise way to create lists in python; compact and easier to read than traditional loops
# expression for value in iterable if condition

doubles = []

for x in range(1,11):
    doubles.append(x * 2)

print(doubles)

doubles1 = [x*2 for x in range(1,11)]   # list comprehension
print(doubles1)

doubles3 = [x*3 for x in range(20,40)]
print(doubles3)

