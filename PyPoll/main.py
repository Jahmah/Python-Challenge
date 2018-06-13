import os
import csv

#Set filepath and import csv file
csvpath = os.path.join('C:\\','Users','Nii','Homework','PyPoll','raw_data','election_data_2.csv')
with open(csvpath, newline = '') as csvfile:
    csvdata = csv.reader(csvfile, delimiter = ',')
    header = next(csvdata)
    
    #Create lists
    voterid = []
    county = []
    candidates = []
    names_of_candidates = []


    #Run a for loop for every row of data
    for row in csvdata:
        voterid.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
    
    #Create variables. 
    voters_list = len(voterid)
    candidates_list = set(candidates) #Set function is used to identify each unique candidate


    print("Election Results")
    print("-----------------------------------------------")
    print(f"The Total number of votes cast: {voters_list}")
    print("------------------------------------------------")



  
    for row in candidates_list:
        names_of_candidates.append(row)

    #Create a dictionary for the candidates
    dict_of_candidates = {}
    candidates_count = 0
    for row in names_of_candidates:
        candidate_name = str(names_of_candidates[candidates_count])
        votes = int(candidates.count(candidate_name))
        vote_share = round(votes/voters_list * 100, 2)
        dict_of_candidates.update({candidate_name: votes})
        print(f"{candidate_name}: {vote_share}%  ({votes})")
        candidates_count = candidates_count + 1

    

    winner = max(dict_of_candidates, key=lambda key: dict_of_candidates[key])
    
    print("--------------------")
    print("Winner: ", winner)
    print("--------------------")


output_path = os.path.join('C:\\','Users','Nii','Homework','PyPoll','Election_results.txt') 
with open(output_path, 'w') as output_file:
    output_file.write("Election Results" + "\n")
    output_file.write("---------------------------------------------------" + "\n")
    output_file.write("The Total number of votes cast: " + str(voters_list) + "\n")
    output_file.write("---------------------------------------------------" + "\n")
    output_file.write(str(names_of_candidates[0]) + ": " + str(round(candidates.count(names_of_candidates[0])/voters_list * 100, 2)) + "%" + " (" + str(candidates.count(names_of_candidates[0])) + ")" + "\n" )
    output_file.write(str(names_of_candidates[1]) + ": " + str(round(candidates.count(names_of_candidates[1])/voters_list * 100, 2)) + "%" + " (" + str(candidates.count(names_of_candidates[1])) + ")" + "\n" )
    output_file.write(str(names_of_candidates[2]) + ": " + str(round(candidates.count(names_of_candidates[2])/voters_list * 100, 2)) + "%" + " (" + str(candidates.count(names_of_candidates[2])) + ")" + "\n" )
    output_file.write(str(names_of_candidates[3]) + ": " + str(round(candidates.count(names_of_candidates[3])/voters_list * 100, 2)) + "%" + " (" + str(candidates.count(names_of_candidates[3])) + ")" + "\n" )
    output_file.write("--------------------------" + "\n")
    output_file.write("Winner: " + str(winner) + "\n")
    output_file.write("--------------------------" + "\n")

    output_file.close






