# SYNTAX: {key: value for item in iterable}

numbers = [1, 2, 3, 4]

squares = {n: n * n for n in numbers}
print(squares)


names = ["mona", "rahul", "shivani"]
name_lengths = {name: len(name) for name in names}

print(name_lengths)