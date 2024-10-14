import random

"""
Give a 10 question test
generate a random index within range of the number of questions
Prompt the student with the question and input their answer
convert their answer to lower case (note all tuple answers are in lower case)
check to see if their answer is in the tuple of possible corresponding answers
keep track of correct and incorrect answers
Example:
  What is a primary color?red
  Words that ryme with bear?pear
  What is a primary color?blue
  Name a famous President?Lincoln
  What is a primary color?red
  Name a season?fall
  Give a math operation?addition
  Give a math operation?subtraction
  Words that ryme with bear?spare
  Words that ryme with bear?dare

  correct:  10 , incorrect: 0
"""
# questions is a list of Strings
questions = [
    "Give a math operation",
    "What is a primary color",
    "Name a famous President",
    "Name a season",
    "Words that ryme with bear",
]

# answers is a list of tuples
answers = [
    ("addition", "subtraction", "multiplication"),
    ("red", "yellow", "blue"),
    ("washington", "jefferson", "lincoln"),
    ("winter", "spring", "summer", "fall"),
    ("tear", "care", "spare", "dare", "mare", "pear"),
]

correct = 0
incorrect = 0

for x in range(5):
    index = random.randint(0, len(questions))
    user_answer = input(questions[index] + ": ")
    user_answer = user_answer.lower()
    if user_answer in answers[index]:
        print("correct")
        correct += 1
    else:
        print("incorrect")
        incorrect += 1

print(f"correct: {correct} , incorrect: {incorrect}")
