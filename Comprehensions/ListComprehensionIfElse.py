numbers = [1, 2, 3, 4, 5]

labels = ["even" if n % 2 == 0 else "odd" for n in numbers]

print(labels)


# Filtering: "if" comes at the end; example: [n for n in numbers if n % 2 == 0] ; filtering what to print (Which item)
# Transformation: "if-else" comes before "for" (deciding what value to put for every item)  ; deciding what "value" to print for every item