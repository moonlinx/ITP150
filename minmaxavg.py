# Initialize variables
max = -1
min = 999
count = 0
total = 0
userNumber = 0
while userNumber >= 0:
    userNumber = int(input("enter number:"))
    if userNumber >= 0:
        total += userNumber
        count += 1
        if userNumber <= min:
            min = userNumber
        if userNumber >= max:
            max = userNumber

print(f"min: {min}, max: {max}, avg: {total/count}")

# capture the maximum number, minimum number and the average number
# averaage == add the numbers and divide by the number of entries
