# Dictionaries in Python

# Dictionaries are stored with key - value pairs
subjects_and_grades = {"Chemistry": 97, "Physics": 94, "Algebra": 90, "Creative Writing": 87}
print(subjects_and_grades)

# Dictionaries can contain lists, but the lists can only be the values - not the keys
families = {"Solomon": ["Dick", "Harry", "Sally", "Tommy"], 
"Brady": ["Greg", "Peter", "Bobby", "Marcia", "Jan", "Cindy"]}
print(families)

inventory = {"stapler": 1, "pens": 5, "tape": 1, "calculator": 1}
print(inventory)

# Adding an item to a dictionary
inventory["monitor"] = 1
print(inventory)

# Modifying an item in a dictionary
inventory["pens"] = 6
print(inventory)

# Removing an item from a dictionary
removed_item = inventory.pop("tape")
print(removed_item)
print(inventory)

# Adding multiple items to a dictionary
inventory.update({"keyboard": 1, "mouse": 1, "usb_drive": 2})
print(inventory)

# Dict comprehensions
food = ["hamburger", "french fries", "turkey sandwich", "grilled cheese"]
print(food)
calories = [550, 500, 230, 390]
print(calories)

# Converts the zipped lists into a dictionary using list comprehension
food_and_calories = {food:calorie for food, calorie in zip(food, calories)}
print(food_and_calories)

# Making a list with the dictionary keys
food_list = list(food_and_calories)
print(food_list)

# Looping through a dictionary
for food in food_and_calories.keys(): # Prints out the keys of the dictionary
    print(food)

for calories in food_and_calories.values(): # Prints out the values of the dictionary
    print(calories)

for food, calories in food_and_calories.items(): # Prints out the keys and values of the dictionary
    print("The " + food + " has/have " + str(calories) + " calories")