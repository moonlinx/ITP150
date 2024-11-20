import random

students = ['Bill', 'Jamie', 'Carter', 'Lisa', 'Faith', 'Thomas']

def createList(numGrades,minG,maxG):
    nList = []
    for i in range(numGrades):
        val = random.randint(minG,maxG)
        nList.append(val)
    return nList

def populate_dictionary(dict, sList):
    minG = 0
    # Iterate through each student in the list
    for student in sList:
        # Create a list of 5 random grades between minG and 100 for the student
        # Store this list as the value for the student's name key in the dictionary
        dict[student] = createList(5,minG,100)
        minG += 10

sDictionary = {}
populate_dictionary(sDictionary, students)

def process_dictionary(dict):
    for student in dict.keys():
        print(dict[student])
