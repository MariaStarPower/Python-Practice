# Loops in Python

# For loops
fruits = ["apple", "banana", "mango", "papaya", "grapefruit"]

for fruit in fruits:
    print(fruit)

# For loops using the range function
for num in range(10):
    print(num) # Prints numbers from 0 - 9

for i in range(5):
    print("Hello Python loops") # Prints "Hello Python loops" 5 times

# While loops
count = 1

while count <= 10:
    print(count)
    count += 1

countdown = 10

while countdown >= 1:
    print(countdown)
    countdown -= 1
print("We have liftoff!")

names = ["Freddy", "Tommy", "Billy", "Sally"]

length = len(names)
index = 0

while index < length:
    print("Hello " + names[index])
    index += 1

# Break statements
for num in range(10):
    if num == 5: # Exits the loop once it reaches 5
        break
    print(num)

# Continue statements
for num in range(20):
    if num % 2 == 0: # Skips over the even numbers
        continue
    print(num)

# Nested loops
sales_lists = [[15, 22, 17], [33, 20, 15], [19, 12, 27]]
sales_total = 0

for list in sales_lists: # Outer loop - iterates through the items in the outer list
    print(list)
    for sale in list: # Inner loop - iterates through each element in the nested lists
        sales_total += sale

print(sales_total)

# List comprehensions
num_list = [1, 2, 3, 4, 5]
print(num_list)

nums_times_2 = [num * 2 for num in num_list] # Multiplies each item by 2 and stores it in a new list
print(nums_times_2)

# List comprehensions with conditionals
numbers = [-1, 0, -5, 6, 10, 16, -22, 3]
print(numbers)
positives = [num for num in numbers if num >= 0] # Stores only the positive numbers into a new list
print(positives)