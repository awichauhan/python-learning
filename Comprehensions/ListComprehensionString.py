# Printing length of words/strings inside a list

words = ["apple", "banana", "cat", "dog"]

lengths = [len(word) for word in words]
print(lengths)

# Uppercase only long words

words = ["apple", "banana", "cat", "dog"]

long_words = [word.upper() for word in words if len(word) > 3]
print(long_words)

