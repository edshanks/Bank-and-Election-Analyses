import os
import csv

filepath = os.path.join("Resources", "election_data.csv")

#total vote counter
vote_count = 0

#list of candidates
candidates = []

#temporary lists for candidate names and number of votes received
can_names = []
can_votes = []

# dictionary of candidates and corresponding vote counts
cand_dict = {}

with open(filepath, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvfile)

    #loop through data to count total votes and determine candidates
    for row in csvreader:
        
        #counts total number of votes
        vote_count = vote_count + 1

        #adds candidates' names to a list
        if row[2] not in candidates:
            #adds name to candidate list
            candidates.append(row[2])
            #adds individual vote count next to candidate name
            candidates.append(1)

        else:
            name = candidates.index(row[2])
            
            #adds one vote to individual vote count for a given candidate
            candidates[name+1] = candidates[name+1] + 1

#splits candidates list into 2 lists for names and number of votes
for i in range(0, len(candidates),2):
    can_names.append(candidates[i])
    can_votes.append(candidates[i+1])

#zips can_names and can_votes into single dictionary
master_dict = dict(zip(can_names, can_votes))



print(master_dict)


print("Election Results")
print("")
print("----------------------------")            
print("")
print(f'Total Votes: {vote_count}')
print("")
print("----------------------------")            
print("")

for x in master_dict:
    #calculates a candidate's votes as % of total votes
    vote_share = (master_dict[x] / vote_count) * 100

    #rounds % to 3 decimal places
    vote_share = round(vote_share, 3)

    print(f' {x}: {vote_share}% ({master_dict[x]})')
    print("")


print("----------------------------")            
print("")

#gets the name with the highest number of votes
winner = max(master_dict, key=master_dict.get)

print(f'Winner: {winner}')
print("")
print("----------------------------")   

################################################################################


#writes results onto new text file
output_path = os.path.join("Analysis", "poll_results.txt")

with open(output_path, 'w') as textfile:

    textfile.writelines("Election Results")
    textfile.writelines('\n')
    textfile.writelines("")
    textfile.writelines('\n')
    textfile.writelines("----------------------------") 
    textfile.writelines('\n')
    textfile.writelines("")
    textfile.writelines('\n')
    textfile.writelines(f'Total Votes: {vote_count}')
    textfile.writelines('\n')
    textfile.writelines("")
    textfile.writelines('\n')
    textfile.writelines("----------------------------")  
    textfile.writelines('\n')
    textfile.writelines("")
    textfile.writelines('\n')
    
    for x in master_dict:
        #calculates a candidate's votes as % of total votes
        vote_share = (master_dict[x] / vote_count) * 100

        #rounds % to 3 decimal places
        vote_share = round(vote_share, 3)

        textfile.writelines(f' {x}: {vote_share}% ({master_dict[x]})')
        textfile.writelines('\n')
        textfile.writelines("")
        textfile.writelines('\n')


    textfile.writelines("----------------------------")
    textfile.writelines('\n')
    textfile.writelines("")
    textfile.writelines('\n')
    textfile.writelines(f'Winner: {winner}')
    textfile.writelines('\n')
    textfile.writelines("")
    textfile.writelines('\n')
    textfile.writelines("----------------------------")

            



       


