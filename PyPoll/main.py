import os
import csv

# Initialise variablews - Required
total_votes = 0
candidates = []
vote_percentage = []
won_votes = []
winner = ""

# Initialise variables - Helper
candidate_column = []
most_votes = 0

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

# Get the total number of votes won by each candidate
for candidate in candidates:
    won_votes.append(candidate_column.count(candidate))

# Get the percentage of votes each candidate won
for index, vote in enumerate(won_votes):
    vote_percentage.append(round(100*vote/total_votes, 3))

    # Get the candidate with the most votes
    if (vote > most_votes):
        most_votes = vote
        winner = candidates[index]

# Format results for printing to terminal and text file
line1 = "Election Results"
line2 = 25*"-"
line3 = f"Total Votes: {total_votes}"
print(total_votes)
print(candidates)
print(won_votes)
print(vote_percentage)
print(most_votes)
print(winner)

# Set variable for output file
# election_result = os.path.join("./PyPoll/analysis", "election_results.txt")

# with open(election_result, "w", newline='') as result:
for index, candidate in enumerate(candidates):
    print(f"{candidate}: {vote_percentage[index]}% ({won_votes[index]})")