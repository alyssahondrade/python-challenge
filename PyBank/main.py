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

# Format results for printing to terminal and text file
line1 = "Financial Analysis"
line2 = 28*"-"
line3 = f"Total Months: {total_months}"
line4 = f"Total: ${net_profit}"
line5 = f"Average Change: ${average_change}"
line6 = f"Greatest Increase in Profits: {date_increase} ({greatest_increase})"
line7 = f"Greatest Decrease in Profits: {date_decrease} ({greatest_decrease})"
results_format = [line1, line2, line3, line4, line5, line6, line7]

# Set variable for output file
budget_result = os.path.join("./PyBank/analysis", "PyBank_results.txt")

with open(budget_result, "w", newline='') as result:
    for line in results_format:
        result.write(line + "\n")
        print(line)