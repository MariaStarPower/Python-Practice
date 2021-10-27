# Lists in Python
list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]
combined_list = list_1 + list_2

print(list_1)
print(list_2)
print(combined_list)

fruits = ["apple", "banana", "pear", "peach"]
print(fruits)

# Adding an item to a list
fruits.append("mango")
print(fruits)

# Removing an item from a list
fruits.remove("pear")
print(fruits)

# Inserting an item into a list at a certain index
fruits.insert(2, "watermelon")
print(fruits)

# Removing an item from the end of the list
fruits.pop()
print(fruits)

# Removing an item at a certain index
fruits.pop(1)
print(fruits)

# Modifying an item in the list
fruits[0] = "grapefruit"
print(fruits)

# Accessing an item in the list
second_fruit = fruits[1]
print(second_fruit)

# Two-dimensional lists
my_2d_list = [[1, "Brad"], [2, "John"], [3, "Benjamin"]]
print(my_2d_list)

# Adding an item to a 2D list
my_2d_list.append([4, "Charlie"])
print(my_2d_list)

# Accessing an item from a 2D list
brad = my_2d_list[0][1]
print(brad)

# Adding something to an item in a 2D list
my_2d_list[3].append(False)
print(my_2d_list)

# Removing something from an item 2D list
my_2d_list[3].remove(False)
print(my_2d_list)

# Removing an item from a 2D list
my_2d_list.pop(2)
print(my_2d_list)

# Modifying an element in a 2D list
my_2d_list[2][0] = 3
print(my_2d_list)

# More list methods
a_list = [1, 2, 2, 2, 3, 15, 0, 29, -5, 99]
print(a_list)

# Getting the length of a list
list_length = len(a_list)
print(list_length)

# Counting the number of times an element appears in a list
how_many = a_list.count(2)
print(how_many)

# Getting the first 3 items from the list
first_three = a_list[:3]
print(first_three)

# Getting the last 3 items from the list
last_three = a_list[-3:]
print(last_three)

# Getting list elements starting from a certain index up to (but not including) the ending index
elements_from_2_to_6 = a_list[2:6]
print(elements_from_2_to_6)

# Sorting the items in a list
sorted_list = sorted(a_list)
print(sorted_list)

# Generating lists with the range function
range_list = list(range(1, 11)) # The ending number is not included in the range
print(range_list)

every_other = list(range(2, 12, 2)) # Will print from 2 - 10 in increments of 2
print(every_other)

# Using lists with the zip function
first_names = ["George", "Thomas", "Ronald"]
print(first_names)

last_names = ["Washington", "Jefferson", "Reagan"]
print(last_names)

first_and_last = zip(first_names, last_names) # Creates a zipped object of the 2 lists
first_and_last_list = list(first_and_last) # List function converts the zipped object to a list
print(first_and_last_list)