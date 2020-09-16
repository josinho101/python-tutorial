import csv

#new record to add to csv
newRecord = ["5", "Jason", "IT"]

#open csv in append mode
file = open("sample.csv", "a")

#write to csv file
writer = csv.writer(file)
writer.writerow(newRecord)
file.close()
