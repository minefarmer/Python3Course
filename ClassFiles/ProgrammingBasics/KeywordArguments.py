#  In this example 'age' and 'name' are the keyword.

def print_something(name = "Someone", age = "Unkown"):
    print("My name is", name, "and my age is", age)

print_something(age = 27)  # My name is Someone and my age is 27
print_something(age = 81, name="Carl")  # My name is Carl and my age is 81
