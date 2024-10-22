
# Must initialize the list prior to
numlist = []
for i in range(5):
    num = int(input("Enter a number: "))
    numlist.append(num)
    num += 1

print(max(numlist))

