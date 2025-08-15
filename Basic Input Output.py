# This script executes a series of questions where the user inputs information
# Based on those inputs, this script then displays an output with the results

# This asks the user to input information
first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
mynova_id = input("Enter your myNova id:")
gpa = float(input("Enter your gpa:"))
semesters_completed = int(input("Enter the number semesters completed:"))

# This outputs the result from the inputted information
print("Welcome,", first_name, last_name)
print("Your myNova id is", mynova_id)
print("Congrats on your gpa of", gpa, "!")
print("I see you have completed", semesters_completed, "semesters")