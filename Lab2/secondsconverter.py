"""
Student name: Devin Delaney
Program: given an amount of time in seconds, this program will
display the amount in hours, minutes, and seconds:
note: use // with division so that you get a whole number
example:
Enter total number of seconds:
4148
amount: 4148 == hours: 1 minutes: 9 seconds: 8
"""
amount = input("Enter total number of seconds:\n> ")
seconds = int(amount)

hours = seconds // 3600
minutes = seconds // 60
seconds = seconds % 60

print(f"Amount: {amount} broken down is:\n Hours: {hours}\n Minutes: {minutes}\n Seconds: {seconds}")
