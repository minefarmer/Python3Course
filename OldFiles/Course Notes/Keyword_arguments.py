# Default arguments  6
# Overriding defaults
# 
# 
# 
# def print_something(name = "Someone", age = "Unknown"):  # Default arguments
#     print("My name is ", name, " and my age is ", age)
# print_something(81)  # My name is  81  and my age is  Unknown


# # This does not work to get only age
# def print_something(name = "Someone", age = "Unknown"):
#     print("My name is ", name, " and my age is ", age)
# print_something(None, 81)  # None is a boolean  *** My name is  None  and my age is  81


# This works to override default arguments
def print_something(name = "Someone", age = "Unknown"):
    print("My name is ", name,", and my age is ", age)
print_something(age = 81, name = 'Carl')  # My name is  Carl , and my age is  81