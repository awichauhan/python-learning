# Use enumerate() when you need both: index + value

names = ["Amit", "Riya", "Mona"]

# normal way:

index = 0
for name in names:
    print(index, name)
    index += 1

# better way (comprehensing):

for index, name in enumerate(names):
    print(index, name)
