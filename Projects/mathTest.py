# Project for ITP
""" 
With this project, you will expand on the Math Quiz lab by adding the following features:
• Prompt the user for the number of questions specified by numQuestions
Note: For testing purposes, I might try 5 and 20.
• Add a multiplication option
• Increase the range and offset if the user answers 3 questions correctly in a row
• Measure the time it takes to answer each question and the average for all 10 questions.
• Provide the number of correct answers and a letter grade.
Requirements
You will prompt the user with 10 questions. Each question can be an addition, subtraction, or
multiplication problem. For addition and subtraction, the random operands will have a range
that will start off at 20 and an offset at 5 (each operand can be within 5-24). For multiplication,
the range will be 11 and the offset will be 0 (each operand can be within 0-10).
Project is a math test that gives 10 questions and then takes the amount correct and incorrect and gives a grade at the end
"""
# MAP:
# 1. import random and time modules
# 2. initialize the modules
# 3. set the variables:
#   a. correct guesses
#   b. incorrect guesses
#   c. number of questions
#   d. operands == 2
#   e. problem types = addition, subtraction, multiplication
#   f. need a loop to keep count
#   g. final grade
# 4. Show how many are correct and incorrect and time taken to complete the questions
# 5. Give a grade

import random
import time

# Initialize the random module
random.seed()

# Variables go here
correct = 0
incorrect = 0
startTime = time.time()
endTime = time.time()
userTime = int(endTime - startTime + .5) # Round to nearest second
question_times = []
numQuestions = 15

# Code goes here 

# Loop through questions with operands and problem types
for x in range(numQuestions):
    startTime = time.time()
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

    endTime = time.time()
    userTime = int(endTime - startTime + .5) # Round to nearest second
    question_times.append(userTime)
    print(f"Time taken: {userTime} seconds")

    if correct == 3:
        oper1 = random.randint(10, 20)
        oper2 = random.randint(10, 20)
    elif correct == 6:
        oper1 = random.randint(20, 30)
        oper2 = random.randint(20, 30)

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
print(f"Time taken: {sum(question_times)} seconds")
