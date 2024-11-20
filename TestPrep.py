import random

"""
centered_average(lst)
     input: list of integers with a length greater than 2
     output: average without the smallest and largest element

     example: given [5, 3, 8, 1, 4], you would not include the 1 and 8 and take the average of 3,4,5 => 4.0
"""

def centered_average(lst):
    minVal = min(lst) # Finding the minimum value
    maxVal = max(lst) # Finding the maximum value
    lst.remove(minVal) # Removing the minimum value 
    lst.remove(maxVal) # Removing the maximum value

    return sum(lst) / len(lst) # adding all elements and dividing by the length of the list


random_list = [5, 3, 8, 1, 4]

avg = centered_average(random_list)
print("centered_average",avg)



"""
remove_outliers(lst, minVal, maxVal)
     remove all values in the list that do not fall within the range of minVal and maxVal
     example - given [5, 8, 3, 9, 12, 1, 4], minVal=4 and maxVal=8
               return [5, 8, 4]
               
     you can return the same modified list or you can create a new list
"""
def remove_outliers(lst, minVal, maxVal):
    # minVal = min(lst) # Finding the minimum value
    # maxVal = max(lst) # Finding the maximum value
    for num in lst:
        if num < minVal:
            lst.remove(num)
        elif num > maxVal:
            lst.remove(num)

    return lst


"""
merge(lst1, lst2) - merge 2 lists 
     input: 2 lists
     output: 1 merged list
     example - merge ([1, 3, 5, 7], [2, 4, 6, 8, 10, 12]) 
               return [1, 2, 3, 4, 5, 6, 7, 8, 10, 12]
"""
def merge(lst1, lst2):
    # Function to merge two lists
    # Input: two lists (lst1 and lst2)
    # Output: one merged list

    # Calculate the total length of both input lists
    totLen = len(lst1) + len(lst2)
    
    # Initialize an empty list to store the merged result
    nLst = []
    
    # Initialize indices for traversing lst1 and lst2
    index1 = 0
    index2 = 0

    # Iterate through the total length of both lists
    for index in range(totLen):
        # Add elements from lst1 on even indices, if available
        if index % 2 == 0 and index1 < len(lst1):
            nLst.append(lst1[index1])
            index1 += 1  # Move to the next element in lst1
        # Note: This implementation is incomplete and needs to be fixed
        # to properly merge the two lists
        elif index % 2 == 1 and index2 < len(lst2):
            nLst.append(lst2[index2])
            index2 += 1  # Move to the next element in lst2
        elif index1 < len(lst1):
            nLst.append(lst1[index1])
            index1 += 1
        elif index2 < len(lst2):
            nLst.append(lst2[index2])
            index2 += 1
    
    return nLst

"""
shuffle_lst(lst)
    given a lst, shuffle the list based on a random index
"""

def shuffle_lst(lst):
    random.shuffle(lst)
    return lst
