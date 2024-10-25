"""
name: Devin Delaney
project: list practice
description: practicing lists from w3 schools
"""
# groceryList = ["milk", "bread", "eggs", "apples", "oranges"]
# shoppingList =  ["pampers", 'shirts', 'socks', 'shoes']
#
# groceryList.append("honey")
# print(groceryList) # ['milk', 'bread', 'eggs', 'apples', 'oranges', 'honey']
# if "milk" in groceryList:
#     print("milk is in this list")
# else:
#     print("milk is not in this list")
# groceryList.sort() # ['apples', 'bread', 'eggs', 'honey', 'milk', 'oranges']
# groceryList[2] = "banana"
# print(groceryList) # ['apples', 'bread', 'banana', 'honey', 'milk', 'oranges']
#
# groceryList.extend(shoppingList)
#
# groceryList.clear()
# print(groceryList)
# def get_user_groceries():
#     user_groceries = []
#     while True:
#         item = input("Enter an item (or press Enter to finish):\n> ")
#         if item == "":
#             break
#         user_groceries.append(item)
#         print(f"Added {item} to your list")
#         user_groceries.sort()
#     return user_groceries
#
# print(get_user_groceries())
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

