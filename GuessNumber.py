# Guessing Game
# This allows the user to guess a number between 0 and 31 using the random module
import random

# initialize the random generator
random.seed()

# generate random number 0-31
randomNumber = int(random.random() * 32)

# Set guess to an empty variable to initialize the loop
guess = None

# Set the for loop and give the user 5 tries to guess the number
for x in range(5):
    #NOTE: the range is the number you already know
    # prompt user for a guess, type cast to an integer
    guess = (int(input("Guess a number between 0 and 31: ")))
    # check if guess is correct. If correct then the game is over and the program ends.
    if guess == randomNumber:
        print("You got it!")
        break
        # If wrong then tell them if too high or too low
    elif guess > randomNumber:
        print("Too high")
    elif guess < randomNumber:
        print("Too low")
        # if guess is not an integer, tell them to enter an integer.
        #NOTE: this is for error handling in case someone is being stupid
    elif type(guess) != int:
        print("Please enter an integer")

# if guess is incorrect after 5 tries then tell them they lost and the correct number
#NOTE: You must place the if statement outside of the for loop in order for it to work.
# What matters is that this if statement is not indented, placing it outside the for loop's block.
# The indentation inside of the for loop would make it a part of the entire first if statement
# Thus give you the answer after any incorrect guess
if guess != randomNumber:
     print(f"\nI'm sorry :( you lost... the number was {randomNumber}")

print("Thanks for playing!")
