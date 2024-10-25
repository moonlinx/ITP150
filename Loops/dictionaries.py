"""
Student: Devin Delaney
Date: 2024-10-17
Program: going through dictionaries
"""

# set your variables
choice = 0

# Create Dictionary
thisdict = {"brand": "Ford", 
            "model": "Mustang",
            "year": 1964
            }

while choice != 4:
    choice = int("1..get, 2..set, 3..print, 4..quit")

    if choice == 1:
        print(thisdict["brand"])
    elif choice == 2:
        thisdict["year"] = 2018
    elif choice == 3:
        print(thisdict)
    elif choice == 4:
        break

print("end of the program")

