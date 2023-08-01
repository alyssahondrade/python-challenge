import os
import csv
from statistics import mean

## TEST VALUES ##
test_total_months = 86
test_net_profit = 22564198
test_average_change = -8311.11
test_greatest_increase = 1862002
test_greatest_decrease = -1825558

# Initialise variables
total_months = 0
net_profit = 0
profit_column = [] # hold the profit/losses values for comparison
date_column = [] # hold the date values for finding greatest increase & decrease
changes = [] # list to track changes in profit/losses
average_change = 0 # calculated value using 'changes' list
greatest_increase = 0
greatest_decrease = 0
month_increase = ""
month_decrease = ""

# Import budget_data.csv
budget_csv = os.path.join("./PyBank/resources", "budget_data.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Get header
    csv_header = next(csvreader)
    print(csv_header)

    for row in csvreader:
        # Typecast (str -> int) at the start
        profit = int(row[1])
        # Increment each month to total_months
        total_months += 1

        # Increment net_profit
        net_profit += profit

        # Populate profit_column and date_column
        profit_column.append(profit)
        date_column.append(row[0])

# Find the profit/losses changes
for index, value in enumerate(profit_column):
    profit = int(value)
    if (index > 0):
        change = int(profit_column[index]) - int(profit_column[index-1])
        changes.append(change)

for index, value in enumerate(changes):
    # 'changes' index is shifted left, must use [index + 1] to get correct month
    if (value > greatest_increase):
        greatest_increase = value
        month_increase = date_column[index+1]

    if (value < greatest_decrease):
        greatest_decrease = value
        month_decrease = date_column[index+1]

average_change = round(mean(changes), 2)
# greatest_increase = max(changes)
# greatest_decrease = min(changes)

print(total_months)
print(net_profit)
#print(changes)
print(f"{greatest_increase} occurred on {month_increase}")
print(f"{greatest_decrease} occurred on {month_decrease}")
print(average_change)

print(len(changes))