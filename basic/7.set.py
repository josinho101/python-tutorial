# Can change set just like list
# will add items to start to set
# Cant access items in a set with index
# set cant hold duplicate items

mySet = {"Red", "Green", "Blue"}

print(type(mySet))
print(mySet)

# add items to set
mySet.add("Orange")
print(mySet)

# check for duplicates
mySet.add("Red")
print(mySet)

# length
print(len(mySet))

# remove
# Error will happen if we try to remove item that is not present
mySet.remove("Orange")
print(mySet)

# discard
# wont give error if we try to discard an item that is not presnet
mySet.discard("Orange")
print(mySet)

print(dir(mySet))