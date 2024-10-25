import math
import statistics

# Function to calculate the mean (average) of a list of numbers
# numList = [6,2,3,1]
# total = sum(numList)
# count = len(numList)
# mean = total / count
#
# # Calculate sum of each item - mean
# def calculate_mean(numList):
#     return sum(numList) / len(numList)
# # Function to calculate the standard deviation
# def calculate_standard_deviation(numList):
#     # Step 1: Calculate the mean
#     mean = calculate_mean(numList)
#
#     # Step 2: Calculate the squared differences from the mean
#     squared_diff = [(x - mean) ** 2 for x in numList]
#
#     # Step 3: Calculate the average of the squared differences
#     variance = calculate_mean(squared_diff)
#
#     # Step 4: Take the square root of the variance
#     std_dev = math.sqrt(variance)
#
#     return std_dev
#
# # Main program
# if __name__ == "__main__":
#     # Example list of numbers
#     data = [2, 4, 4, 4, 5, 5, 7, 9]
#
#     # Calculate and print the standard deviation
#     result = calculate_standard_deviation(data)
#     print(f"The standard deviation of {data} is: {result:.2f}")

# Summary of how the code works:
# 1. We define two functions: calculate_mean() and calculate_standard_deviation().
# 2. calculate_mean() simply adds up all the numbers and divides by the count.
# 3. calculate_standard_deviation() follows these steps:
#    a. Calculate the mean of the numbers.
#    b. Calculate the squared differences from the mean for each number.
#    c. Calculate the average of these squared differences (variance).
#    d. Take the square root of the variance to get the standard deviation.
# 4. In the main program, we create a sample list of numbers.
# 5. We call calculate_standard_deviation() with our sample data.
# 6. Finally, we print the result, rounded to 2 decimal places.

data = [2, 4, 4, 4, 5, 5, 7, 9]

stats = statistics.mean(data)
print(f"mean of the data is {stats}")
