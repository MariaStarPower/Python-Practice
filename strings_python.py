# Strings in Python

favorite_fruit = "strawberry" # String stored in a variable
print(favorite_fruit)
# Gets the length of the string
string_length = len(favorite_fruit)
print(string_length)
# Counts how many times a certain character appears in a string
r_count = favorite_fruit.count("r")
print(r_count)
# Gets the first character of the string
print(favorite_fruit[0])
# Gets the character at the fourth index of the string
print(favorite_fruit[4])
# Gets the character at the last index of the string
print(favorite_fruit[-1])
# Gets the character at the second-to-last index of the string
print(favorite_fruit[-2])
# Gets the first five characters of the string
print(favorite_fruit[:5])
# Gets the last five characters of the string
print(favorite_fruit[5:])
# Gets the last three characters of the string
print(favorite_fruit[-3:])
# Gets the characters starting at the fourth index up to, but not including, the sixth index
print(favorite_fruit[5:7])

# String concatenation
first = "apple"
second = "sauce"
first_and_second = first + second
print(first_and_second)

first_name = "Donald"
last_name = "Reagan"

# Modifying a string using slicing
fixed_first_name = "R" + first_name[1:]
print(fixed_first_name + " " + last_name)

# Iterating through strings
def print_each_letter(word): # Function that prints each letter of the word
    for letter in word:
        print(letter)

print_each_letter("pineapple")

# Strings and conditionals
def letter_in_word(word, letter):  # Function that checks if a letter is in the word
    for char in word:
        if char == letter:
            return True
    return False

r_in_word = letter_in_word("strawberry", "r") # Returns True
print(r_in_word)
z_in_word = letter_in_word("strawberry", "z") # Returns False
print(z_in_word)

def letter_count(word, letter): # Function that counts how many times a letter appears in the word
    count = 0
    for char in word:
        if char == letter:
            count +=1
    return count

r_count = letter_count("strawberry", "r") # Returns 3
print(r_count)
w_count = letter_count("strawberry", "w") # Returns 1
print(w_count)
z_count = letter_count("strawberry", "z") # Returns 0
print(z_count)

print("e" in "blueberry") # Prints True
print("x" in "blueberry") # Prints False

def common_letters(string1, string2): # Function that returns the letters that are common for both words
    common_list = []
    for letter in string1:
        if (letter in string2) and not (letter in common_list):
            common_list.append(letter)
    return common_list

print(common_letters("pineapple", "applesauce")) # Returns [p, e, a, l]

def even_indexes(word): # Function that returns the letters at the even indexes of the word
    evens = []
    for i in range(len(word)):
        if i % 2 == 0:
            evens.append(word[i])
    return evens

print(even_indexes("watermelon"))
print(even_indexes("cantaloupe"))

print("watermelon".find("a")) # Returns the index of the specified letter
print("watermelon".replace("a", "@")) # Replaces the first character with the second one

long_string = "This is a long string"
print(long_string)

split_string = long_string.split(" ") # Splits the string into a list by the spaces between each word
print(split_string)

rejoined_string = "_".join(split_string) # Rejoins the list into a string with the underscore between each word
print(rejoined_string)

name = "Johnny"

print(name.upper()) # Prints JOHNNY
print(name.lower()) # Prints johnny
print(name.title()) # Prints Johnny