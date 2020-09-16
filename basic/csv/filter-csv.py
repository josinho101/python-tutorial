import csv

file = open("sample.csv" ,"r")
reader = csv.reader(file, delimiter = ",")

for row in reader:
    if row[2] == "IT":
        print(row)


file.close()
