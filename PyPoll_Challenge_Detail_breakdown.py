# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join(".","Resources", "election_results.csv")

# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis_detailed.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}


# 1: Create a county list and county votes dictionary.
counties = []
counties_dict = {}
county_votes={}

# create dictionary for summation
votes={}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county = ""
### Ian's note: does not technically need to initialize this variable here; would be clearer to initialize further down; 
county_voter_turnout = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Extract the county name & candidate name from each row.
        county_name = row[1]
        candidate_name = row[2]
        # tally total votes
        total_votes += 1

        # create the list of counties
        if county_name not in counties:
            counties.append(county_name)
        
        # Create the list of candidates
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

    # initialize empty dictionaries
    for candidate in candidate_options:
        votes[candidate]=0
        candidate_votes[candidate]={}
    
    # fill dictionaries
    for county in counties:
        # initialize county_votes by county
        votes[county]=0
        for candidate in candidate_options:
            candidate_votes[candidate][county]=0
    
    election_data.seek(0)
    next(reader)

    # For each row in the CSV file
    for row in reader:
        # pull county name & candidate
        county_name = row[1]
        candidate_name = row[2]
        # tally vote by county name and candidate
        candidate_votes[candidate_name][county_name]+=1
        votes[county_name]+=1
        votes[candidate_name]+=1
        
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)
    
    for county in counties:

        # Calculate the percentage of votes for the county.
        vote_percentage = float(votes[county])/float(total_votes)*100
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes[county]:,})"
        )
    
        # 6d: Print the county results to the terminal.
        print(county_results)

        # 6e: Save the county votes to a text file.
        txt_file.write(county_results+"\n")

        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes[county]>county_voter_turnout) and (vote_percentage > winning_percentage):
                county_voter_turnout = votes[county]
                largest_county = county
        largest_county_summary = (
            f"\n-------------------------\n"
            f"Largest County Turnout: {largest_county}\n"
            f"-------------------------\n"
        )
        
    # 7: Print the county with the largest turnout to the terminal.
    print(largest_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_summary)       


    # candidate breakdown
    for candidate in candidate_options:
        candidate_breakdown = ""
        
        for county in counties:
            candidate_by_county_perc = float(candidate_votes[candidate].get(county)/float(votes[county]))*100
            perc_of_votes_rec = (float(candidate_votes[candidate].get(county))/float(votes[candidate]))*100
            candidate_breakdown = (candidate_breakdown + f"\n       {county}- {candidate_votes[candidate].get(county):,}, {candidate_by_county_perc:.2f}% of county; {perc_of_votes_rec:.2f}% of votes received")
            
            vote_percentage = float(votes[candidate]) / float(total_votes) * 100
            candidate_results = (
                f"{candidate}: {vote_percentage:.1f}% total ({votes[candidate]:,} total){candidate_breakdown}\n")
        
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
            
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes[candidate] > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes[candidate]
            winning_candidate = candidate
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
