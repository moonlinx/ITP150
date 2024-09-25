import random

# initialize the random generator
random.seed()

# generate random number 0-31
randomNumber = int(random.random() * 32)
guess = None

# for loop - 5 iterations
for x in range(5):
    #NOTE: the range is the number you already know
    # prompt user for a guess, cast to an integer
    guess = (int(input("Guess a number between 0 and 31: ")))
    # check if guess is correct. If correct then the game is over
    if guess == randomNumber:
        print("You got it!")
        break
        # If wrong then tell them if too high or too low
    elif guess > randomNumber:
        print("Too high")
    elif guess < randomNumber:
        print("Too low")
    elif type(guess) != int:
        print("Please enter an integer")

# if guess is incorrect after 5 tries then tell them they lost and the correct number
#NOTE: you need extra space away from the previous loop in order for the if statement to actually work
if guess != randomNumber:
     print(f"\nI'm sorry :( you lost... the number was {randomNumber}")

print("Thanks for playing!")
