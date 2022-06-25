# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# intilalize a total vote counter.
total_votes = 0

# candidate options
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# winning candidate and winning count tracker
winning_candidate =""
winning_count = 0
winning_percentage = 0


# open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # read the header row
    headers = next(file_reader)

    # print each row in csv file
    for row in file_reader:
        # add to the total vote count.
        total_votes += 1

        # print the candidate name from each row.
        candidate_name = row[2]

        #if the candidate does not match any existing candidates...
        if candidate_name not in candidate_options:
          
            #add it to the list of candidates.
             candidate_options.append(candidate_name)

             # 2. begin tracking that candidate's vote count.
             candidate_votes[candidate_name] = 0

         # add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:
    # 2. retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    
    # 3. calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # to do: print out each candidate's name. vote count, and percentage of
    # votes to the terminal

    # determine winning vote count and candidate
    # determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # and, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
        
        #to do : print out the winning candidate. vote count and percentage to
        # terminal
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)    


    







