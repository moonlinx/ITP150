priceBurgers = 5.25
priceFries = 2.75
# prompt user for number of burgers
numBurgers = input("Enter number of burgers:") # numBurgers is a String
numBurgers = int(numBurgers) # numBurgers is an integer
# prompt user for number of fries and convert variable to an integer
numFries = int(input("Enter number of fries:"))
# compute cost
total = numBurgers * priceBurgers + numFries * priceFries
# display number of burgers and fries, and the total cost
'''
note, you can print multiple items
by seperating with a comma (',')
'''
print(f" num burgers: {numBurgers}\n num fries: {numFries}\n total cost: ${total}")
