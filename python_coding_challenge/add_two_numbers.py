import operator

# Without user input
num1 = 8
num2 = 7
sum = num1 + num2
print("Sum of", num1, "and", num2, "is", sum)

# With user input
num3 = input("Enter the first number: ")
num4 = input("Enter the second number: ")
sum = float(num1) + float(num2)
print("Sum of", num3, "and", num4, "is", sum)


# Defining function
def add(a, b):
    return a + b


num5 = 6
num6 = 7
print("Add two numbers using function:", num5, "and", num6, "is", add(num5, num6))

# Using operator.add() method

num7 = 10
num8 = 43
print("Add two numbers using operator add method:", num5, "and", num6, "is", operator.add(num7, num8))

# Using lambda function

num9 = 23
num10 = 56
add_number = lambda a, b: a + b
print("Add two numbers using lambda function:", num5, "and", num6, "is", add_number(num9, num10))

# Using