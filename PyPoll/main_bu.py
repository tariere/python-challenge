#to start, I'll import the modules that I will need to access the data in the file and manipulate the data in the CSV.
import os
import csv
#importing a specific tool from the collections module. this counter will help my count the rows in the csv per candidate.
from collections import Counter

#I'll place the path the the CSV in a variable so that it can be referenced
election_csv = os.path.join("Resources", "election_data.csv")
#check this
#print(election_csv)

#access the csv file, and put the contents in a variable called csvreader
with open(election_csv, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")


    csv_header = next(csvreader)
    #just a check to make sure I'm getting the values I want for the headers in a list
    #print (csv_header)

    #I want to to take a quick look at the contents of my csv.
    #print(csvreader)
    # It's to big, so I can't, womp womp.  Need to look into a way to take a peek. 

    #I'm also going to set up my script to print the output right away as soon as the values are obtained. They will export to a report called poll_report.txt
    outputpath = os.path.join("poll_report.txt")    
    with open (outputpath, 'w') as report:

        #This will tally the occurances of a particular candidate in my fields and put them in a dictionary called election counts.  The keys will be the values of the column in the csv (candiate) and the values will be the result of the counter.
        electioncounts = Counter()
        for row in csvreader:
            electioncounts[row[2]] += 1
        
        #check the results of the above to see if they look expected. 
        #print (electioncounts)

        #This is just to print the text/formatting elements of my report before I get to specific values.  This goes for any text only other text only print commands in the script as well. 
        print("Election Results")
        print("----------------------------")
        
        print("Election Results", file=report)
        print("----------------------------", file=report)
        
        #Now that I have a dictionary of the data I want, I'm using the below line to get a sum total of all of the values for each of the keys in my dictionary.  This will give me the total number of votes casts.
        totals = sum(electioncounts.values())
        print(f'Total Votes: {totals}')
        print("----------------------------")
        
        print(f'Total Votes: {totals}', file=report)
        print("----------------------------", file=report)

        #I've created a loop that will print out the key and the value for each candidate found in the list.  Before it prints though, it will do a quick calculation of the percentage of votes per candidate and insert that in the correct location in the loop.
        for key, value in electioncounts.items():
            perc = round((value/totals)*100)
        
            print(f'{key}: {perc}.000% ({value})')
            print(f'{key}: {perc}.000% ({value})', file=report)

        print("----------------------------")
        print("----------------------------", file=report)
        
        #I'm using the .get() method to obtain the keyvalue of the max value in my election counts dictionarys, as this will tell me who received the most votes and won the election.
        keymax = max(electioncounts, key=electioncounts.get)
        print(f'Winner: {keymax}')
        print(f'Winner: {keymax}', file=report)

        # outputpath = os.path.join("poll_report.txt")    
        # with open (outputpath, 'w') as report:
        #     # Here', I'm going to export the data to a text file
        #     print("Election Results", file=report)
        #     print("----------------------------", file=report)
        #     print(f'Total Votes: {totals}', file=report)
        #     print("----------------------------", file=report)
        #     print(f'{key}: {perc}.000% ({value})', file=report)
        #     print("----------------------------", file=report)
        #     print(f'Winner: {keymax}', file=report)








    
    