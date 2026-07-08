# Generator does not create the full list immediately. It produces values one by one.
# Generators are useful when data is large.
numbers = [1, 2, 3, 4]

squares = (n * n for n in numbers)

print(squares)

for value in squares:
    print(value)


total = sum(n * n for n in range(1000000))
for x in total:
    print(x)