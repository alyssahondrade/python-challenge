import os
import csv

# Initialise variablews - Required
total_votes = 0
candidates = []
vote_percentage = []
won_votes = []

# Import election_data.csv
election_csv = os.path.join("./PyPoll/resources", "election_data.csv")

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Get header
    csv_header = next(csvreader)
    
    for row in csvreader:
        total_votes += 1

        if row[2] not in candidates:
            candidates.append(row[2])

print(total_votes)
print(candidates)