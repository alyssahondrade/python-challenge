import os
import csv

# Import election_data.csv
election_csv = os.path.join("./PyPoll/resources", "election_data.csv")

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Get header
    csv_header = next(csvreader)
    print(csv_header)