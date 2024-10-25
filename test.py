numList = [7,4,1,3,9,8,6,5,2,0]
print(numList)
numList.sort()
print(numList)

while True:
    num = int(input("Enter a number to add to the list: "))
    if num == -1:
        break
    numList.append(num)
    numList.sort()
    print(numList)
