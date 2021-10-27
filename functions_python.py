# Functions in Python

def print_hello(): # Function that prints "Hello" without any parameters
    print("Hello")

print_hello() # Calls the function

def greeting(name): # Function that prints out a greeting with a parameter of name
    print("Hello " + name)

greeting("Sam") # Calls the function with an argument for name
greeting("Johnny")

a = 5
b = 10

def add_nums(num1, num2): # Function that takes in parameters and returns a result
    return num1 + num2

print(add_nums(a, b))

num_list = [37, 19, 17, 33, 49]
print(num_list)

def get_average(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)

average = get_average(num_list) # Function calls can be stored in a variable
print(average)