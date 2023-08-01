import os
import csv

# Import budget_data.csv
budget_csv = os.path.join("./PyBank/resources", "budget_data.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Get header
    csv_header = next(csvreader)
    print(csv_header)