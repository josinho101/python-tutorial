# dictionary is a key value paired collection

myD = {1281: "Joseph", 2281: "Lincy", 3281: "Dileep"}

print(type(myD))
print(myD)

# access items with key
print(myD[1281])

# add items
myD[4281] = "Logan"
print(myD)

# length
print(len(myD))

# change value of an item
myD[3281] = "John"
print(myD[3281])
print(myD)

print(dir(myD))