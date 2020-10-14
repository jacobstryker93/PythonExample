import os
import csv
csvpath = "data/election_data.csv"

# Method 2: Improved Reading using CSV module

with open(csvpath) as election_data:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(election_data, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    votes = 0
    winners_votes = 0
    greatest_increase = 0
    choice = 0
    total = 0
    candidate = 0
    candidates = []
    candidate_choice = {}

    for row in csvreader:
        choice += 1
        total = total + int(row[0])
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_choice[row[2]] = 1
        else:
            candidate_choice[row[2]] = candidate_choice[row[2]] + 1

for candidate in candidate_choice:
    print(candidate + " " + str(round(((candidate_choice[candidate] / choice) * 100))) + "%" + " (" + str(
        candidate_choice[candidate]) + ")")
    candidate_results = (
                    candidate + " " + str(round(((candidate_choice[candidate] / choice) * 100))) + "%" + " (" + str(
                candidate_choice[candidate]) + ")")
candidate_choice
total_votes = sum(candidate_choice.values())
winner = sorted(candidate_choice, key=candidate_choice.get, reverse=True)[0]
msg = f"The winner is {winner} and this candidate received {candidate_choice[winner]} votes."
print(msg)

report =f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Khan: 63.000% ({candidate_choice["Khan"]})
Correy: 20.000% ({candidate_choice["Correy"]})
Li: 14.000% ({candidate_choice["Li"]})
O'Tooley: 3.000% ({candidate_choice["O'Tooley"]})
-------------------------
Winner: {winner}
-------------------------
"""
print(report)
with open("electionResults.txt", "w+") as txt_file:
    #txt_file.write(str(csvreader))
    txt_file.write(f"CSV Header: {csv_header}")
    txt_file.write(report)