import csv

#open file
file = open("sample.csv", "r")
#read csv content
reader = csv.reader(file, delimiter = ",")

#print content
for row in reader:
    print(row)

#close file
file.close()
