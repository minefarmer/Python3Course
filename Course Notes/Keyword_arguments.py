def print_something(name = "Someone", age = "Unknown"):
    print("My name is", name, "and my age is", age)
print_something(age = 81)  # My name is Someone and my age is 81  ** age is the keyword argument
print_something(age = 81, name="Carl")  # My name is Carl and my age is 81  ** this change the order of the result.
