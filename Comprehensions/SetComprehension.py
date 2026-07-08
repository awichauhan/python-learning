# Set removes duplicates automatically; also unordered


numbers = [1, 2, 2, 3, 3, 4]

unique_squares = {n * n for n in numbers}
print(unique_squares)

set1 = {x * 2 for x in numbers}
print(set1)