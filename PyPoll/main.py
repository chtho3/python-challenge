# Import Modules
import csv 
import numpy as np 

# Open CSV file
csv_path = "Resources/election_data.csv"

with open(csv_path, newline="") as csvfile:
    election_csv = csv.reader(csvfile,delimiter=",")
# Pop-off the header
    election_header = next(election_csv)
#print(election_header)

# Count number of votes cast
    vote_tally = 0
    for row in election_csv:
       vote_tally = vote_tally + 1
    #print(vote_tally)

# Count the list of candidates
with open(csv_path, newline="") as csvfile:
    election_csv = csv.DictReader(csvfile,delimiter=",")
    full_candi_list = []
    for line in election_csv:
        full_candi_list.append(line['Candidate'])
    candi_list = np.unique(full_candi_list)
    #print(candi_list)

# Calculate the total number and % votes each candidate won
with open(csv_path, newline="") as csvfile:
    election_csv = csv.DictReader(csvfile,delimiter=",")
    correy_count = 0
    khan_count = 0
    li_count = 0
    otooley_count = 0
    for line in election_csv:
        if line['Candidate'] == candi_list[0]:
            correy_count = correy_count + 1
        elif line['Candidate'] == candi_list[1]:
            khan_count = khan_count + 1
        elif line['Candidate'] == candi_list[2]:
            li_count = li_count + 1
        elif line['Candidate'] == candi_list[3]:
            otooley_count = otooley_count + 1
    
    #candi_dict = {
    #    candi_list[0] : correy_count,
    #    candi_list[1] : khan_count,
    #    candi_list[2] : li_count,
    #    candi_list[3] : otooley_count
    #}
    #print(candi_dict)
    percent_correy = (correy_count / vote_tally) * 100
    percent_khan = (khan_count / vote_tally) * 100
    percent_li = (li_count / vote_tally) * 100
    percent_otooley = (otooley_count / vote_tally) * 100

    #print(percent_otooley)


# Determine the winner
    percent_list = [percent_correy, percent_khan, percent_li, percent_otooley]
    max_percent = np.max(percent_list)
    win_candi_index = percent_list.index(max_percent)
    win_candi = candi_list[win_candi_index]
    #print(win_candi)
    #print(max_percent)

# Hmm I could probably chain these three lists into a dictionary and sort
# them by vote count instead of in alphabetical order. :\

# Print results to the terminal
    print("Election Results")
    print("---------------------------")
    print(f'Total Votes: {vote_tally}')
    print("---------------------------")
    print(f'{candi_list[0]}: {np.round(percent_list[0],3)}% ({correy_count})')
    print(f'{candi_list[1]}: {np.round(percent_list[1],3)}% ({khan_count})')
    print(f'{candi_list[2]}: {np.round(percent_list[2],3)}% ({li_count})')
    print(f'{candi_list[3]}: {np.round(percent_list[3],3)}% ({otooley_count})')
    print("---------------------------")
    print(f'Winner: {win_candi}')
    print("---------------------------")

# Save the output file
with open("output.txt", "w") as text_file:
    text_file.write("Election Results \n")
    text_file.write("--------------------------- \n")
    text_file.write(f'Total Votes: {vote_tally} \n')
    text_file.write("---------------------------\n")
    text_file.write(f'{candi_list[0]}: {np.round(percent_list[0],3)}% ({correy_count}) \n')
    text_file.write(f'{candi_list[1]}: {np.round(percent_list[1],3)}% ({khan_count}) \n')
    text_file.write(f'{candi_list[2]}: {np.round(percent_list[2],3)}% ({li_count}) \n')
    text_file.write(f'{candi_list[3]}: {np.round(percent_list[3],3)}% ({otooley_count}) \n')
    text_file.write("--------------------------- \n")
    text_file.write(f'Winner: {win_candi} \n')
    text_file.write("--------------------------- \n")