# This program plays the classic game of Rock, Paper, Scissors where the user can play against the program
# Given the user's input a random choice will be genereated by the program
# The program will loop until the user wins against the program

# This imports the random module allowing for a random choice to be generated
import random

# This variable keeps the game running until the user is victorious
user_won = False

# This starts a loop that runs until the user is victorious
while not user_won:
    
    # This asks the user for their choice of rock, paper, or scissors
    print("Enter 1 for Rock, 2 for Paper, 3 for Scissors:")
    user = int(input())
    
    # This generates a number between 1 to 3
    computer = random.randint(1, 3)

    # This shows what the user inputed into the terminal
    if user == 1:
        print("You chose rock")
    elif user == 2:
        print("You chose paper")
    elif user == 3:
        print("You chose scissors")

    # This shows a response based on the number that is randomly generated not by the user
    if computer == 1:
        print("The computer chose rock")
    elif computer == 2:
        print("The computer chose paper")
    elif computer == 3:
        print("The computer chose scissors")

    # This checks if a draw is in place
    if user == computer:
        print("You tied. Try again!\n")
    
    # This verifies who is victorious
    elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
        print("Congrats, you won! Goodbye.")
        user_won = True  # This stops the loop
    
    # If a victor or tie is not had then this will attempt for a retrial
    else:
        print("You lost. Try again!\n")
