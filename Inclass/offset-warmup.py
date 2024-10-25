'''
Given a list of integers, find the numbers that fit within the offset and range
range = 5
offset = 10
'''

mrange = 5
offset = 10
count = 0
myVals = []
numList = [9, 12, 14, 15 , 3, 6, 10]
low = offset
high = offset + mrange - 1

for k in range(len(numList)):
    if numList[k] >= low and numList[k] <= high:
        count += 1
        myVals.append(numList[k])

print("count=", count, "myVals=", myVals)
