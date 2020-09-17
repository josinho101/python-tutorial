import os

#get current working directory
print(os.getcwd())

print("--------------------------")

#list all files and directories
print(os.listdir())

print("--------------------------")

desktop = "c:/users/josinho/desktop"

#change working directory
os.chdir(desktop) #path to desktop.
print(os.getcwd())
print(os.listdir())

print("--------------------------")

#create directory
os.chdir(desktop)
print(os.listdir())
os.makedirs("test_dir")
print(os.listdir())

#create a file
file = open("test_file.txt", "x")
file.close()

print("--------------------------")

#check if a file exist
print(os.path.isfile("test_file.txt"))

print("--------------------------")

#check if a folder exist
print(os.path.isdir("test_dir"))

#remove file
os.remove("test_file.txt")

#remove directory
os.removedirs("test_dir")

