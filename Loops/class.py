# thislist = ["apple", "cherry", "kiwi"]
#
# thislist.insert(2, "abc")
# print(thislist)
#
# thislist.append("abc")
# print(thislist)
#
# thislist.remove("abc")
# print(thislist
#
myFridge =  ["apple", "cherry", "kiwi"]
while True:
    item = input("What would you like to add? ")
    if item == "e":
        break
    else:
        myFridge.append(item)
print(myFridge)
