# Dependencies
import csv
import os

# Files to Load - Input File
election_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

# Open and Read the csv
with open(election_csv) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)

# Initialize Variable
    total_votes = 0

# Creating Empty Dictionary to Store Candidate and Votes
    poll_count = {}

# Read Through Values and Add Them to Dictionary
    for row in reader:
        total_votes += 1 # Adds to Vote Count for Specific Candidate
        if row[2] in poll_count.keys():
            poll_count[row[2]] = poll_count[row[2]] + 1
        else:
            poll_count[row[2]] = 1 # Resets Vote for New Candidate

# Creating Empty Lists for Candidates and Votes
candidates = []
number_votes = []
vote_percent = []
winner = []

# Adding Values to Lists
for key, value in poll_count.items(): # Accessing Keys and Corresponding Value 
    candidates.append(key)
    number_votes.append(value)

# Vote Percent List
for x in number_votes:
    vote_percent.append(round(x/total_votes*100, 3))
            
# Combining All Data (Candidates, Number of Votes, Percentage) into Tuple
data = list(zip(candidates, number_votes, vote_percent))

# Figuring out the Winner By Comparing All Data
for name in data:
    if max(number_votes) == name[1]:
        winner.append(name[0])

#Print Results
print("Election Results\n")
print("-" * 30 + "\n")
print(f"Total Votes: {total_votes}\n")
print("-" * 30 + "\n")
print(f"{candidates[0]}: {vote_percent [0]}% ({number_votes[0]})\n")
print(f"{candidates[1]}: {vote_percent [1]}% ({number_votes[1]})\n")
print(f"{candidates[2]}: {vote_percent [2]}% ({number_votes[2]})\n")
print("-" * 30 + "\n")
print(f"Winner: {winner}\n")
print("-" * 30)
      
#Generate Text File and Output
election_analysis = os.path.join("PyPoll", "analysis", "election_analysis.txt")

with open(election_analysis, "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("-" * 30 + "\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-" * 30 + "\n")
    text_file.write(f"{candidates[0]}: {vote_percent [0]}% ({number_votes[0]})\n")
    text_file.write(f"{candidates[1]}: {vote_percent [1]}% ({number_votes[1]})\n")
    text_file.write(f"{candidates[2]}: {vote_percent [2]}% ({number_votes[2]})\n")
    text_file.write("-" * 30 + "\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("-" * 30 + "\n")

