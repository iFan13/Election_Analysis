# Election_Analysis

## Project Overview

Tom and Seth of the Colorado Board of Elections has given the following tasks to be completed for an election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Get a complete list of counties who had voters.
4. Calculate the total number of votes each candidate received.
5. Calculate the total number of voters each county had.
6. Calculate the percentage of votes each candidate won.
7. Determine the winner of the election via popular vote.

## Resources

- Data source: election_results.csv
- Software: Python 3.9.1, Visual Studio code 1.52.1

## Election-Audit Results

The analysis of the election show that

- There were 369,711 votes cast in the election.
- The counties were:
  - Jefferson county at 10.5% of the votes and 38,855 number of votes
  - Denver county at 82.8% of the votes and 306,055 number of votes
  - Arapahoe county at 6.7% of the votes and 24,801 number of votes
- Denver county had the largest number of votes.
- The candidates & their results were
  - Charles Casper Stockham receiving 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette receiving 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane receiving 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette, who received 272,892 number of votes and had a winning 73.8% of votes.

Results are also downloadable [here](/analysis/election_analysis.txt)

## Election-Audit Summary

The python script attached [here](/PyPoll_Challenge.py) could potentially be further modified depending on the data sets provided. In the above for [this dataset](/Resources/election_results.csv), county, candidate are tabulated separately. However, it is possible to delve into greater detail and granularity to count for votes for specific candidates within a county (ie: what is the split of votes in each county for each candidate). This can be done using an dictionary within a dictionary. Conversely, it would also be possible to tabulate popularity of the candidate within a specific county (ie: which candidate won in each county). An example of the script and results that does both would can be found within this respository. [Script](/PyPoll_Challenge_Detail_breakdown.py) and [sample result](/analysis/election_analysis_detailed.txt)

It is also possible to increase the complexity and scalability of the script by using the built in `os.walk()` method to go through the entire resources folder and create a list of CSVs to analyze and output an individual analysis by creating a new `file_to_save` path name based on the input, per CSV file. The starting sample of this scalability can be found [here](/PyPoll_Challenge_Increase_Scale.py). The limitation of this would be that each column in the CSV files must be the same field and field types.

Other ways the script can be used would be to add additional fields and checks for fields however that would be reliant on the data set.
