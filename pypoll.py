#In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
#(Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. 
#Your task is to create a Python script that analyzes the votes and calculates each of the following:
    #The total number of votes cast
    #A complete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #The winner of the election based on popular vote.

#importing libraries
import csv
import os

#path to feed in csv data
csvpath = os.path.join("election_data.csv")

#setting variables and make empty lists. 

votetotal = 0
mostvotes = 0

candidates = []
votespercandidate = {}
percent = {}


#reading thru csv data, skipping header
with open(csvpath, "r") as electiondata:
    reader = csv.reader(electiondata, delimiter = ",")
    header = next(reader)

    for readerdata in reader:
        nameofcandidate = readerdata[2]
        votetotal = votetotal + 1
        #stores names of candidatesan
        if nameofcandidate not in candidates:
            candidates.append(nameofcandidate)
            votespercandidate[nameofcandidate] = 0
        #vote tally
        votespercandidate[nameofcandidate] = votespercandidate[nameofcandidate] + 1
    #prints out total votes
    electionresults = (
        f"---------------------------------"
        f"\nElection Results"
        f"\n---------------------------------\n"
        f"Total Votes: {votetotal}"
        f"\n---------------------------------\n"
    )
    #finds and prints total votes per candidate in a breakdown
    for candidate in votespercandidate:
        candidatevote = votespercandidate.get(candidate)
        percent[candidate] = round(candidatevote / votetotal*100,2)

        candidatebreakdown = (f"{candidate}: {candidatevote}, {percent[candidate]}%\n")
        electionresults = electionresults + candidatebreakdown

        #finds candidate w most votes
        if candidatevote > mostvotes:
            mostvotes = candidatevote
            winner = candidate
        
        winnerbreakdown = (
            f"Winner: {winner}"
            )

    #adds winner info to election results
    electionresults = electionresults + winnerbreakdown
           
#prints out complete election results        
print(electionresults)

#sets output path to txt file
outputpath = os.path.join("electionresults.txt")

with open(outputpath, "w") as txt_file:
    txt_file.write(electionresults)