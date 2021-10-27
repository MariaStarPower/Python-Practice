# Basic Python

# Printing an integer number
print(1)

# Printing a float number
print(3.6)

# Printing an arithmetic operation
print(1 + 1)

# Printing a word
print("Hi")

# Storing a number in a variable
favorite_number = 5

# Storing arithmetic operations in variables
add = 2 + 1
subtract = 2 - 1
multiply = 2 * 4
divide = 20 / 5
modulus = 14 % 3
exponent = 2 ** 4

# Storing strings in variables
greeting = "Hi"
name = "Maria"

# Printing the stored variables
print(favorite_number)
print(add)
print(subtract)
print(multiply)
print(divide)
print(modulus)
print(exponent)
print(greeting)
print(name)

# Printing multiple strings
print(greeting + " " + name)

# Block text
block_text = """
    This is how you represent block
    text in Python.  Here is some more
    block text.  More block text.  More
    block text.
"""
print(block_text)

# Boolean operations
print("5 > 2 evaluates to True: " + str(5 > 2))
print("5 < 2 evaluates to False: " + str(5 < 2))
print("-1 <= 0 evaluates to True: " + str(-1 <= 0))
print("1 >= 5 evaluates to False: " + str(1 >= 5))
print("1 == 1 evaluates to True: " + str(1 == 1))
print("1 == 4 evaluates to False: " + str(1 == 4))
print("10 != 11 evaluates to True: " + str(10 != 11))
print("10 != 10 evaluates to False: " + str(10 != 10))

# Combined boolean statements with AND
combined_boolean_1_and = (4 + 1 <= 5) and (6 + 2 == 8) # True
combined_boolean_2_and = (-1 > 0) and (2 < 3) # False
combined_boolean_3_and = (6 >= 5) and (5 - 1 < 2) # False
combined_boolean_4_and = (1 + 1 > 2) and (5 != 5) # False

print(combined_boolean_1_and)
print(combined_boolean_2_and)
print(combined_boolean_3_and)
print(combined_boolean_4_and)

# Combined boolean statements with OR
combined_boolean_1_or = (4 + 1 <= 5) or (6 + 2 == 8) # True
combined_boolean_2_or = (-1 > 0) or (2 < 3) # True
combined_boolean_3_or = (6 >= 5) or (5 - 1 < 2) # True
combined_boolean_4_or = (1 + 1 > 2) or (5 != 5) # False

print(combined_boolean_1_or)
print(combined_boolean_2_or)
print(combined_boolean_3_or)
print(combined_boolean_4_or)

# Boolean statements with NOT
not_boolean_1 = not (1 + 1 == 4) # True
not_boolean_2 = not (2 + 2 <= 4) # False

print(not_boolean_1)
print(not_boolean_2)

# If/Else statements
x = 7

if (x >= 10):
    print(str(x) + " is greater than or equal to 10")
else:
    print(str(x) + " is not greater than or equal to 10")

a = 5
b = 5

if (a > b):
    print(str(a) + " is greater than " + str(b))
elif (a < b):
    print(str(a) + " is less than " + str(b))
else:
    print(str(a) + " and " + str(b) + " are equal")