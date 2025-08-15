# This script executes a series of variables where values are assigned by the developler
# Based on the inputs from the developer, this script then dispalys different data types

# This is the value assignment to each variable 
name = "John Doe"   # str
age = 24            # int
height = 5.11       # float

# This outputs the results from the inputted values
print("Literal string:", name)
print("Literal integer:", age)
print("Literal float:", height)

# This asks the user to input information
user_str = input("Enter a string: ")
user_int = int(input("Enter an integer: "))
user_float = float(input("Enter a float: "))

# This outputs the results from the inputted information
print("You entered the string:", user_str)
print("You entered the integer:", user_int)
print("You entered the float:", user_float)

# This outputs the type () of function that was inputted
print("The type of user_str is:", type(user_str))
print("The type of user_int is:", type(user_int))

print("The type of user_float is:", type(user_float))
