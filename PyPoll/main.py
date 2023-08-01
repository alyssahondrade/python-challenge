import os
import csv

# Initialise variablews - Required
total_votes = 0
candidates = []
vote_percentage = []
won_votes = []

# Initialise variables - Helper
candidate_column = []

# Import election_data.csv
election_csv = os.path.join("./PyPoll/resources", "election_data.csv")

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Get header
    csv_header = next(csvreader)
    
    for row in csvreader:
        # Get the total number of votes cast
        total_votes += 1

        # Get list of candidates who received votes
        if row[2] not in candidates:
            candidates.append(row[2])
        
        # Populate candidate_column
        candidate_column.append(row[2])

for candidate in candidates:
    won_votes.append(candidate_column.count(candidate))
    

print(total_votes)
print(candidates)
print(won_votes)