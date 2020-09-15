#open file

file1 = open("employees.txt", "r")
#read all data
print(file1.read())

print("------------------------------")

file2 = open("employees.txt", "r")

#read specified charectors
print(file2.read(10))


print("------------------------------")

file3 = open("employees.txt", "r")

#read a single line
print(file3.readline())
print(file3.readline())
print(file3.readline())
print(file3.readline())

print("------------------------------")

#read file using loop
file4 = open("employees.txt", "r")

for x in file4:
    print(x.strip())

