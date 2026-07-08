# Use zip() when you want to combine two or more lists item by item.

names = ["Amit", "Riya", "Mona"]
marks = [80, 90, 85]

for name, mark in zip(names, marks):
    print(name, mark)

# CREATING DICTIONARIES:
keys = ["name", "age", "city"]
values = ["Mona", 27, "Bangalore"]

data = dict(zip(keys, values))

print(data)