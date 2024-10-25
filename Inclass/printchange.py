
"""
Student name: Devin Delaney
Program: given an amount of money, this program will display the amount in change:
quarters, dimes, nickels, and pennies
NOTE: use // with division so that you get a whole number

The text prompts the user to enter an amount, converts it to pennies, and then calculates the number of quarters, dimes, nickels, and pennies in that amount. It also includes comments and warnings about potential errors in the calculations.
"""

amount = input("Enter amount:\n")
pennies = float(amount) * 100
pennies = int(pennies + 0.5) # adding .5 prevents truncations errors
# if you input 1.13, python stores it as 112.999999999
#TODO: figure out how many quarters , then use the mod (%) to determine what is left over
# when the quarters are removed. Then figure out the number of dimes and nickels using the same process

quarters = pennies // 25
dimes = pennies // 10
nickels = pennies // 5
pennies = pennies % 25
dimes = dimes % 10
#WARNING: if you divide by 0, you will get infinity.

print(f"amount: {amount}\nquarters: {quarters}\ndimes: {dimes}\nnickels: {nickels}\npennies: {pennies}")

