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
    for student in sList:
        dict[student] = createList(5,minG,100)
        minG += 10

sDictionary = {}
populate_dictionary(sDictionary, students)

def process_dictionary(dict):
    for student in dict.keys():
        print(dict[student])
