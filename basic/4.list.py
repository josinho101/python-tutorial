myList = ["Red", "Green", "Blue"]

print(type(myList))
print(myList)
print(myList[1])

# list constructor
myData = list(("data1", "data2", "data3"))

print(type(myData))
print(myData)
print(myData[1])

# add items to list
myList.append("Orange")
print(myList)

# find length of list
print(len(myList))

# reverse a list
myList.reverse()
print(myList)

# remove item from list
myList.remove("Orange")
print(myList)

# clear a list
myList.clear()
print(myList)