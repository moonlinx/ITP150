"""
MathQuiz.py
Student: Devin Delaney

Generate a loop with numQuestions iterations.
    Generate 2 random operands with each having a range of 0-9
    Generate a random number 0 or 1
       0: addition problem
       1: subtraction problem
    Prompt the User with questions
    Compare the User's answer with the correct answer
    Display the result and display the correct answer if they got it wrong
    Maintain 2 counters: correct and incorrect.  Increment the appropriate counter

Display the result of the 10 question quiz:
   number of correct and incorrect

Example output:
what is 6 + 9? 14
incorrect, answer is:  15
what is 2 - 4? -2
correct!
what is 9 - 3? 6
correct!
  ...
what is 4 + 7? 11
correct!

results:
   correct = 8
   incorrect = 2

"""

import random

# initialize the random generator
random.seed()

correct = 0  # number of correct questions answered
incorrect = 0  # number of incorrect questions answered
numQuestions = 10

for x in range(numQuestions):
    oper1 = int(random.randint(0, 9) * 10)
    
    oper2 = int(random.randint(0, 9) * 10)

    # generate a random number for 2 options: addition or subtraction
    problemtype = int(random.randint(0,1))

    # if addition, generate a question for oper1 + oper2
    if problemtype == 0:
        answer = oper1 + oper2
        print(f"what is {oper1} + {oper2}?")
    # else (i.e. subtraction) generate a question for oper1 - oper2
    else:
        answer = oper1 - oper2
        print(f"what is {oper1} - {oper2}?")
    # display the results of the question and display the answer only if they got it wrong
    
    # increment correct or incorrect


# after the loop, display the results:  num of correct and incorrect

