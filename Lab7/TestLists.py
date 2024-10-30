import random
import math
"""
    printList

    input: an list of integers
    output: (void)

    display all elements within an list, 4 spaces per element
    print a new line after every 10 elements
"""
def printList(msg, lst):

    print(f"{msg} :")
    for k in range(len(lst)):
        print(f"{lst[k]:4d}  ", end="")
        if (k + 1) % 10 == 0:
            print()
    print()

"""
    populateList
    	input:  length, range, and an offset
		output: list
    
        create the list with the given length, then populate 
        each element with the given range and offset:  
               offset <= x < offset+range  
"""
def populateList(length, rnge, offset):
    nList = []
    for k in range(length):
        val = int(random.random() * rnge + offset)
        nList.append(val)
    return nList


"""
    countOdd_Over50
		input: an list of integers
		output:  a count of elements that are odd AND greater than 50

       countOdd_Over50 ( [6, 51, 90, 61, 12, 14] ) => 2

import math
       create and initialize a count variable to 0.
       traverse the list and test for odd AND over 50
       
	   return the count
"""

def countOdd_Over50(lst):
    cnt = 0
    for k in lst:
        if k % 2 == 1 and k > 50:
            cnt += 1
    return cnt


"""
    replaceNegatives
		input: an list of integers
		output: none, but the contents of the list may change

			modify the existing list.  If an element is negative, replace
    		it with the absolute value.

        replaceNegatives ( [6, 25, -8, 9, -12, -8] ) => [6, 25, 8, 9, 12, 8]
"""

def replaceNegatives(lst):
    for k in lst:
        if k < 0:
            k = abs(k)
    return lst


"""
    def withinRange(lst, offset, rnge):

		input: an list of integers, offset, and range
		output: count of elements within the specified offset and range

			count the number of elements within the specified offset and range
            example: if the offset is 5 and the range is 3, count the number of 
                     elements that are within 5-7  (5,6,7)

        withinRange ( [12, 14, 9, 2, 10, 6], 10, 5 ) => 3
"""
def withinRange(lst, offset, rnge):
    cnt = 0
    for k in lst:
        if k >= offset and k < offset + rnge:
            cnt += 1
    return 0



"""
    calculateAverage
		input:  list of integers
		output: average value

       calculateAverage ( [10, 11, 12, 13] ) => 11.5

       create a sum
       traverse the list
          add the element to sum

       divide the sum by the number of elements - use the len() function
       return the average
"""

def calculateAverage(lst):
    sum = 0
    for k in lst:
        sum += k
    return sum / len(lst) 


"""
    calculate the standard deviation
		input: a list of integers
		output: standard deviation 

       use the formula:
          https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-population/a/calculating-standard-deviation-step-by-step
              
       use math.sqrt(z) to take the square root.
"""


def computeStandardDeviation(lst):
    # call your calculateAverage method
    #
    # compute the standard deviation
    return 0


#
#  complete the functions and then test with the code below
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
printList("test", myList)

nList = populateList(40, 90, 20)
printList("nList", nList)

# test your countOdd_Over50 function
print("odd and greater than 50: ", countOdd_Over50(nList))

# test your replaceNegatives function
nList = populateList(40, 50, -25)
printList("nList", nList)
replaceNegatives(nList)
printList("after replaceNegatives", nList)


# to test withinRange
nList = [12, 14, 9, 2, 10, 6]
printList("nList", nList)
print("withinRange, offset = 10, range = 5: ", withinRange(nList, 10, 5))


# to test the average and standard deviation, use a fixed list so you will know the results are correct
avg = calculateAverage(myList)
print("average: ", avg)

myList = [6, 2, 3, 1]
sd = computeStandardDeviation(myList)
print("standard deviation is: ", sd)
