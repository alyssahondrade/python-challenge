import os
import csv
from statistics import mean

# Initialise variables - Required
total_months = 0
net_profit = 0
average_change = 0 # calculate value using 'changes' list
greatest_increase = 0
greatest_decrease = 0
date_increase = ""
date_decrease = ""

# Initialise variables - Helpers
profit_column = [] # hold the profit/losses values for comparison
date_column = [] # hold the date values for finding greatest increase & decrease
changes = [] # list to track changes in profit/losses

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

# Get the average change
average_change = round(mean(changes), 2)

# Find the greatest increase/decrease, and corresponding date
for index, value in enumerate(changes):
    # 'changes' index is shifted left, must use [index + 1] to get correct month
    if (value > greatest_increase):
        greatest_increase = value
        date_increase = date_column[index+1]

    if (value < greatest_decrease):
        greatest_decrease = value
        date_decrease = date_column[index+1]

## TEST ##
error_count = 0

## TEST VALUES ##
test_total_months = 86
test_net_profit = 22564198
test_average_change = -8311.11
test_greatest_increase = 1862002
test_greatest_decrease = -1825558
test_date_increase = "Aug-16"
test_date_decrease = "Feb-14"

# Confirm correct value for total_months
if (total_months != test_total_months):
    error_count += 1
    print(f"'Total Months' should be: {test_total_months}. "
          + f"Your value is: {total_months}.")

# Confirm correct value for net_profit
if (net_profit != test_net_profit):
    error_count += 1
    print(f"'Total' should be: {test_net_profit}. "
          + f"Your value is: {net_profit}.")

# Confirm correct value for greatest_increase
test_greatest_increase = max(changes)
if (greatest_increase != test_greatest_increase):
    error_count += 1
    print(f"'Greatest Increase' should be: ${test_greatest_increase}. "
          + f"Your value is: ${greatest_increase}.")

# Confirm correct value for greatest_decrease
test_greatest_decrease = min(changes)
if (greatest_decrease != test_greatest_decrease):
    error_count += 1
    print(f"'Greatest Decrease' should be ${test_greatest_decrease}. "
          + f"Your value is: ${greatest_decrease}.")

# No errors, print results to text file AND terminal
if (error_count == 0):
    print("Financial Analysis")
    print(28*"-")
    print(f"Total Months: {total_months}")
    print(f"Total: {net_profit}")

    print(f"{greatest_increase} occurred on {date_increase}")
    print(f"{greatest_decrease} occurred on {date_decrease}")
    print(average_change)