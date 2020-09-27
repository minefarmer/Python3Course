import re

print("Our Magical Caculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = input("Enter equation:")
    if previous == 0:
        equation = input("enter equation:")
    else:
        equation = re.sub('[a-zA=Z,.:()" "]', '', equation)

    if previous == 0:
        previous == eval(equation)
    else:
        previous = eval(str(previous) + equation)


        print("You typed", previous)

while run:
    performMath()
