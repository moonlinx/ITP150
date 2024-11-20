"""
Student: Devin Delaney
Date: 2024-11-18
Project: Calculate your grade average

Instructions:
You will create and fill out lists for each Grade Category and put them into a dictionary.
You’ll have at least 2 functions:
 - Populate the dictionary – populate your dictionary with the lists of your current grades
 - Compute the final grade – compute the average for each category and display the weighted and
letter grade

➢ You must have at least 2 functions, defined above. You are encourage to use more.
➢ You must use a formatted print statement for the output defined above
➢ You can hard code your grades when you populate the dictionary
➢ When calculating the average and grade percentage, you must traverse your dictionary,
using the following for loop.
for category in dict.keys():
- use category as the key and as a String for display and looking up the
grade percentage (ex: 65%)
"""
# 1. Create two main functions: `populate()` and `final()`.
# 2. Use lists to store grades for each category.
# 3. Use a dictionary to store these lists, with category names as keys.
# 4. Implement the `populate()` function to create and return this dictionary.
# 5. Create an average for grades like the last hw assignment - Take from there if necessary
# 5. Implement the `final()` function to calculate the average for each category and the final grade.
    # Have section in final to iterate through dictionary
# 6. Use formatted print statements for output.
# 7. Use a for loop to traverse the dictionary when calculating averages and percentages.

#NOTE: Ensure to include Type annotations so you don't forget what needs to happen

# Define a function that returns a dictionary and stores grade categories adn their corresponding scores
# Function to populate the grades dictionary
def populate() -> dict[str, list[float]]:
    # Create a dictionary with grade categories as keys and lists of grades as values
    grades = {
        "Exams": [85.0, 90.0, 88.5],
        "Projects": [92.0, 88.0, 95.0],
        "Midterm Quizzes": [78.5, 85.0, 82.0],
        "Labs": [95.0, 98.0, 100.0, 97.5],
        "In-class Quizzes": [90.0, 85.5, 88.0, 92.0]
    }
    return grades  # Return the grades dictionary for use in other functions

# Function to calculate the average of a list of grades
def calculate_average(grades: list[float]) -> float:
    # Sum all grades and divide by the number of grades
    return sum(grades) / len(grades)

# Function to determine the letter grade based on a percentage
def get_letter_grade(percentage: float) -> str:
    # Use if-elif-else statements to return the appropriate letter grade
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

# Function to calculate the final grade and letter grade
def final(grades: dict[str, list[float]]) -> tuple[float, str]:
    total_percentage = 0
    # Dictionary of weights for each category
    weights = {
        "Exams": 0.65,
        "Projects": 0.20,
        "Midterm Quizzes": 0.05,
        "Labs": 0.05,
        "In-class Quizzes": 0.05
    }

    # Iterate through each category in the grades dictionary
    for category in grades.keys():
        # Calculate the average grade for the category
        average = calculate_average(grades[category])
        # Calculate the weighted average for the category
        # WARNING: This wasn't completely correct! Please double check before submission!
        weighted_average = average * weights[category]
        # Add the weighted average to the total percentage
        total_percentage += weighted_average
        # Print the category, average, and grades
        print(f"""
        category       Average    Grades
        --------       -------    ------

        {category}     {average:.2f}, {grades[category]}""")
    #NOTE: I couldn't figure out this part 

    # Get the letter grade based on the total percentage
    letter_grade = get_letter_grade(total_percentage)
    # Return the total percentage and letter grade as a tuple
    return total_percentage, letter_grade

# Main part of the script
grades = populate()  # Get the grades dictionary
final_grade, letter_grade = final(grades)  # Calculate the final grade and letter grade by passing both variables into the final grade function
print(f"\nFinal Grade: {final_grade:.2f}%")  # Print the final grade percentage
print(f"Letter Grade: {letter_grade}")  # Print the letter grade
