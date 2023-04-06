import os 
import csv

filepath = os.path.join("Resources", "budget_data.csv")

#month count
months_count = 0

#profit/loss summation
PL = 0

#stores PL monthly values
PL_list = []

#stores PL dates (month/year)
PL_list_date = []

with open(filepath, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvfile)

    for row in csvreader:
        #counts number of months
        months_count = months_count + 1

        #sums P/L's
        PL = PL + int(row[1])

        #adds month/year to PL_list
        PL_list_date.append(row[0])

        #adds P/L's to PL_list
        PL_list.append(int(row[1]))

#PL change month to month
PL_change = []

#date of each PL monthly change
PL_change_date = []

n = 0
#loops through PL_list and calculates monthly changes
for month in range(1, len(PL_list)):

    change = PL_list[month] - PL_list[month-1]

    date = PL_list_date[month-1]
    
    #adds month/year to PL_change_date list
    if n == 0:          #skips first date
        n = n + 1
        
    else:
        PL_change_date.append(date)

    #adds values to list of monthly changes
    PL_change.append(change)

#calculates average of month to month changes
length = len(PL_change)
sum = sum(PL_change)
average = sum / length

#prints desired values to the terminal

print("Financial Anaysis:")
print("")
print("---------------------------")
print("")

print(f"Total Months: {months_count}")          #prints total months

print("")
print(f"Total: ${PL}")                          #prints total profit
print("")

print(f"Average Change: ${round(average, 2)}")  #calculates average change in profit
print("")

max_date = PL_change.index(max(PL_change))      #finds date that corresponds to min profit
print(f"Greatest Increase in Profits: {PL_change_date[max_date]} (${max(PL_change)})")

print("")
min_date = PL_change.index(min(PL_change))      #finds date that corresponds to max profit
print(f"Greatest Decrease in Profits: {PL_change_date[min_date]} (${min(PL_change)})")

