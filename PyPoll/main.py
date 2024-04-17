# Import dependencies
import csv
import os


# Read the data and create an object out of the CSV
election_data = os.path.join("Resources", "election_data.csv")

# Initialize variables
votes_total = 0
candidates = []
votes_count = []
votes_percent = []

# Read the CSV file
with open( election_data, newline = "" ) as csvfile:
    csv_reader = csv.reader( csvfile, delimiter = "," )

    # Store the csv header
    csv_header = next(csv_reader)

    # Iterate through the csv rows
    for row in csv_reader:

        # Count the number of votes
        votes_total += 1

        # Check if the candidate is not in the list
        if row[2] not in candidates:
            
            # Add candidate to the list
            candidates.append( row[2] )
            candidate_index = candidates.index( row[2] )
            
            # Add 1 vote for this candidate in the votes count
            votes_count.append(1)

        else:
            # Find the index of the existing candidate in the list
            candidate_index = candidates.index( row[2] )
            votes_count[candidate_index] += 1


    # Compute the percentage of votes for each candidate
    for count in votes_count:
        candidate_percentage = (count/votes_total)*100
        candidate_percentage = "%.3f%%" % candidate_percentage
        votes_percent.append(candidate_percentage)


    # Find the candidate with the most votes
    winner = max(votes_count)
    index = votes_count.index(winner)
    winner_candidate = candidates[index]

output_text = (
    f"\nElection Results\n"
    f"\n----------------------------\n\n"
    f"Total Votes: {votes_total}\n"
    f"\n----------------------------"
    )

for i in range(len(candidates)):
    output_text += f"\n{candidates[i]}: {votes_percent[i]} ({votes_count[i]})"

output_text += (f"\n----------------------------\n\n"
    f"The winner is : {winner_candidate}\n"
    f"\n----------------------------")
    

# Export text file with the analysis
results_txt = os.path.join("analysis", "results.txt")
with open (results_txt, "w") as txt_file:
    txt_file.write(output_text)






        
