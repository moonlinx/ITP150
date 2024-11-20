# Project for ITP
""" 
Student Name: Devin Delaney
Project Name: Math Test
Project Description:
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
# 2. initialize the modules and seed the random module
# 3. set the variables:
#   a. correct guesses
#   b. incorrect guesses
#   c. number of questions
#   d. operands == 2
#   e. problem types = addition, subtraction, multiplication
#   f. need a loop to keep count
#   g. start time
#   h. end time
#   i. time taken
#   j. question times
#   k. number of questions
#   g. final grade
#   l. feedback
# 4. Show how many are correct and incorrect and time taken to complete the questions
# 5. Give a grade
# 6. Give feedback
# 7. Display the results
# 8. End

import random
import time

# Initialize the random module
random.seed()

# Variables go here
correct: int = 0
incorrect: int = 0
startTime: float = time.time()
endTime: float = time.time()
userTime: int = int(endTime - startTime + .5) # Round to nearest second
question_times: list = []
numQuestions: int = int(input("How many questions do you want?\n#: "))

# Variables for difficulty increase
consecutive_correct: int = 0
difficulty_level: int = 0
range_start: int = 0
range_end: int = 10

# Code goes here 

# Loop through questions with operands and problem types
for x in range(numQuestions):
    startTime = time.time()
    oper1 = random.randint(range_start, range_end)
    oper2 = random.randint(range_start, range_end)
    
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
    # Get the user's answer 
    userAnswer = int(input("Your answer: "))

    # Check the answer
    if userAnswer == answer:
        print("Correct!")
        correct += 1
        consecutive_correct += 1

        # For difficulty increase
        if consecutive_correct == 3:
            difficulty_level +=1
            range_start += 5
            range_end += 5
            consecutive_correct = 0
            print(f"Difficulty increased to {difficulty_level}!")
    else:
        print(f"Incorrect the answer was {answer}")
        incorrect += 1
        consecutive_correct = 0

    endTime = time.time()
    userTime = int(endTime - startTime + .5) # Round to nearest second
    question_times.append(userTime)
    print(f"Time taken: {userTime} seconds\n")

# Calculate the grade
grade = (correct / numQuestions) * 100
if grade >= 90:
    grade = "A"
elif grade >= 80:
    grade = "B"
elif grade >= 70:
    grade = "C"
elif grade >= 60:
    grade = "D"
else:
    grade = "F"

# Determine grade feedback
if grade == "A":
    feedback = "Excellent!"
elif grade == "B":
    feedback = "Good job!"
elif grade == "C":
    feedback = "Middeling."
elif grade == "D":
    feedback = "Needs work."
elif grade == "F":
    feedback = "Better luck next time."

# Display the results
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Grade: {grade}")
print(f"Feedback: {feedback}")
print(f"Time taken: {sum(question_times)} seconds")
