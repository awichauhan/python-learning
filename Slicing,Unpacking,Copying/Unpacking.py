# Unpacking means taking values from a list/tuple and storing them into variables.

values = [10, 20, 30, 40, 50]

first, second, *remaining = values  # *remaining means: Put all leftover values into this variable as a list

print(first)
print(second)
print(remaining)


values = ["Mona", "Python", "AI", "ML", "LLM"]

name, current_topic, *future_topics = values

print(name)
print(current_topic)
print(future_topics)


first, *middle, last = [10, 20, 30, 40, 50]  # *middle collects the leftover values between first and last.

print(first)
print(middle)
print(last)

