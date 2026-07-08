names = ["Amit", "Riya", "Mona"]
marks = [80, 90, 85]

for rank, (name, mark) in enumerate(zip(names, marks), start=1):  # zip(names, marks) creates name-mark pairs & enumerate(..., start=1) adds numbering.
    print(rank, name, mark)


# enumerate()  -> adds index
# zip()        -> joins lists together
# sorted()     -> arranges data
# sum()        -> adds numbers
# min()        -> smallest
# max()        -> largest