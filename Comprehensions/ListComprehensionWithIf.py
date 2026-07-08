numbers = [1, 2, 3, 4, 5, 6]

evens = []

for n in numbers:
    if n % 2 == 0:
        evens.append(n)

print(evens)

evens1 = [n for n in numbers if n % 2 == 0]  #  List comprehension with IF using already defined list
evens2 = [x * 2 for x in range(1,11) if x % 2 == 0]   # List comprehension with IF using range function to create from scratch
print(evens1)
print(evens2)


# [expression for item in iterable if condition]

