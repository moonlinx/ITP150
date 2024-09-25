"""
restaurant.py
 @author: Devin Delaney
 Our pizza joint sells only cheese pizzas and uses the following rules:
 Small 1.50 per slice, Whole Pie 8.00
 Medium 1.75 per slice, Whole Pie 10.00
 Large 2.00 per slice, Whole Pie 12.00

 Ask the user to input the size, type, and the quantity.
 They can buy only 1 pie at a time. They can buy 1-8 slices.
 if the type is "whole", the quantity is 1.  Otherwise it's 1-8 (slices)
 charge a 6% sales tax on the total

 You do not have to check for invalid input on this assignment.
"""
print("""Welcome to the Pizza Joint!
----- Menu -----
Small 1.50 per slice, Whole Pie 8.00
Medium 1.75 per slice, Whole Pie 10.00
Large 2.00 per slice, Whole Pie 12.00
You can buy only 1 pie at a time. You can buy 1-8 slices.
----------------""")

"""
variables
    size: "S", "M", "L"
    type: "slice" or "whole"
    if slice, quantity: 1-8
"""

# get input from the user

size = input("What size do you want? (S, M, L): ").upper()
kind = input("What kind of pizza do you want? (slice, whole): ")
quantity = int(input("How many slices do you want? "))
# determine price based on input
if size == "S":
    #prices for small pizza slice
    slice_price = 1.50
    whole_price = 8.00
elif size == "M":
    #prices for medium pizza slice
    slice_price = 1.75
    whole_price = 10.00
elif size == "L":
    #prices for large pizza slice
    slice_price = 2.00
    whole_price = 12.00
else:
    print("Invalid size")

if kind == "slice":
    #price for slice
    price = slice_price
    subtotal = slice_price * quantity
elif kind == "whole":
    #price for whole
    price = whole_price
    subtotal = whole_price * quantity
else:
    print("Invalid kind")

# add a sales tax of 6%
tax = subtotal * 0.06
# display the price and total
print("\n----- Order Summary -----")
print(f"Size: {size}")
print(f"Kind: {kind}")
print(f"Quantity: {quantity}")
print(f"Subtotal: {subtotal}")
print(f"Sales Tax: {tax}")
print(f"Total: {subtotal + tax}")
print("-------------------------")
print("Thank you for your order! Have a nice day!")
