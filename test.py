numList = [7,4,1,3,9,8,6,5,2,0]
print(numList)

while True:
    num = int(input("Enter a number to add to the list or enter 'e' to exit.\n> "))
    if num == -1 or num == 'e':
        break
    numList.append(num)
    numList.sort()
    
print(numList)
