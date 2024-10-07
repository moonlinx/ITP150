# Project for ITP
# Project is a math test that gives 10 questions and then takes the amount correct and incorrect and gives a grade at the end
# MAP:
# 1. import random module
# 2. initialize the module
# 3. set the variables:
#   a. correct guesses
#   b. incorrect guesses
#   c. number of questions
#   d. operands == 2
#   e. problem types = addition, subtraction, multiplication
#   f. need a loop to keep count
#   g. final grade
# 4. Show how many are correct and incorrect
# 5. Give a grade

import random

random.seed()

# Variables go here
correct = 0
incorrect = 0
numQuestions = 10

# Loop through questions with operands and problem types
for x in range(numQuestions):
    oper1 = random.randint(0, 10)
    oper2 = random.randint(0, 10)
    
    # Set the problem types == addition, subtraction, multiplication
    problemType = random.randint(0, 2)

    # if addition, generate a question -> oper1 + oper2
    if problemType == 0:
        answer = oper1 + oper2
        print(f"what is {oper1} + {oper2}?")
    # if subtraction, generate a question -> oper1 - oper2
    elif problemType == 1:
        answer = oper1 - oper2
        print(f"what is {oper1} - {oper2}?")
    # if multiplication, generate a question -> oper1 * oper2
    elif problemType == 2:
        answer = oper1 * oper2
        print(f"what is {oper1} * {oper2}?")
    # display the resutls of the question 
    userAnswer = int(input("Your answer: "))

    # Check the answer
    if userAnswer == answer:
        print("Correct")
        correct += 1
    else:
        print("Incorrect")
        incorrect += 1

# Calculate the grade
grade = (correct / numQuestions) * 100

# Determine grade feedback
if grade >= 90.0:
    feedback = "Congrats"
elif grade >= 80.0:
    feedback = "Good job"
elif grade >= 70.0:
    feedback = "Pretty good"
elif grade >= 60.0:
    feedback = "Not bad"
elif grade >= 50.0:
    feedback = "You can do better"
else:
    feedback = "Better luck next time"

# Display the results
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Grade: {grade:.1f}%")
print(f"Feedback: {feedback}")
