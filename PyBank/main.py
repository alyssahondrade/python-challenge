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
changes = [] # list to track changes in profit/losses
average_change = 0 # calculated value using 'changes' list
greatest_increase = 0
greatest_decrease = 0

# Import budget_data.csv
budget_csv = os.path.join("./PyBank/resources", "budget_data.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Get header
    csv_header = next(csvreader)
    print(csv_header)

    for row in csvreader:
        profit = row[1]
        # Increment each month to total_months
        total_months += 1

        # Increment net_profit, after typecasting to int
        net_profit += int(profit)

        # Populate profit_column
        profit_column.append(profit)

# Find the profit/losses changes
for index, value in enumerate(profit_column):
    if (index > 0):
        change = int(profit_column[index]) - int(profit_column[index-1])
        changes.append(change)

average_change = round(mean(changes), 2)
greatest_increase = max(changes)
greatest_decrease = min(changes)

print(total_months)
print(net_profit)
#print(changes)
print(greatest_increase)
print(greatest_decrease)
print(average_change)