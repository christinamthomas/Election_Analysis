# The data we need to retrieve
    #election_results.csv- code to read csv
import csv

import os

file_to_load= os.path.join("election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    for row in file_reader:
        print(row)



#1. The total number of votes cast

#2. A complete list of candidates who received votes

#3. The percentage of votes each candidate won

#4. The total number of votes each cadidate won

#5. The winner of the election based on popular vote


# close the file
