import os
import csv
PyRoll_csvpath=os.path.join("Resources","election_data.csv")

voter_ID = []
candidates = {}

with open (PyRoll_csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    for row in csvreader:
        voter_ID.append(row[0])
        if row[2] not in candidates:
           candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1


    total_voters=len(voter_ID)
    print(total_voters)
    print(candidates)
    output_file=os.path.join("analysis","analysis.txt")
    with open(output_file, "w") as datafile:
        datafile.write("Election Results\n")
        datafile.write("----------------------------\n")
        datafile.write("Total Votes: " + str(total_voters) + "\n")
        datafile.write("----------------------------\n")

        winner = ""
        winner_votes = 0
        for name, votes in candidates.items():
            percent_votes=round(votes/total_voters *100,4)
            print(name, votes, str(percent_votes) + "%")
            datafile.write(name + ": " + str(percent_votes)+"% (" + str(votes)+")\n")

            if winner_votes < votes:
                winner = name
                winner_votes = votes
        print(winner)
        datafile.write("----------------------------\n")
        datafile.write("Winner: "+(winner)+ "\n")
        datafile.write("----------------------------\n")
            


    
    
    










