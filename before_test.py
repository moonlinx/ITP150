"""
Practice Problems

        1.	Loops
Write a loop to print the square of each number from 1 to 10.
        2.	Functions
Write a function is_even(num) that returns True if num is even, False otherwise.
        3.	Lists
        •	Write a function to find the centered average of a list.
        •	Merge [1, 3, 5] and [2, 4, 6] into a single list.
        •	Write a function to remove the two largest and two smallest elements from a list.
        4.	Dictionaries
        •	Create a dictionary student_grades with names as keys and grades as values. Add a new student.
        •	Write a loop to print each student and their grade.
        •	Modify a student’s grade by key.
"""


# 1
def loop_square():
    for num in range(1, 11):
        print(num**2)
