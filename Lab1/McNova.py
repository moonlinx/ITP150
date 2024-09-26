# Set the prices for the items as the starter point
priceBurgers = 5.25
priceFries = 2.75

# prompt user for number of burgers
numBurgers = input("Enter number of burgers:") # numBurgers is a String
numBurgers = int(numBurgers) # numBurgers is an integer

# prompt user for number of fries and convert variable to an integer
numFries = int(input("Enter number of fries:"))

# compute cost
total = numBurgers * priceBurgers + numFries * priceFries

# Triple quotes is not seen by the interpreter. It is a comment.
'''
note, you can print multiple items
by seperating with a comma (',')
'''

# display number of burgers and fries, and the total cost
print(f" num burgers: {numBurgers}\n num fries: {numFries}\n total cost: ${total}")
