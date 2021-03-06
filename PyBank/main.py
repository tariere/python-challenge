#to start, I'll import the modules that I will need to access the data in the file and manipulate the data in the CSV.
import os
import csv

#I'll place the path the the CSV in a variable so that it can be referenced
budget_csv = os.path.join("Resources", "budget_data.csv")
#check this
#print(budget_csv)

#access the csv file, and put the contents in a variable called csvreader
with open(budget_csv, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")

    #put the header of the csv in a variable and move on to the next row in the csv.
    csv_header = next(csvreader)


    #I'm going to create several variables to store data as I take a look a the the data in the CSV.
    #pddiff will be used to capture /store the differences between the current profit loss value and the previous profit loss value
    pldiff = []

    #pldates will be used to capture the dates in my csv in a list just so that it's easier to manipulate
    pldates = []

    #variable to capture and store the total number of months in the data set
    totalmonths = 0

    #variable to capture the total sum of all of the values in the profit loss colummn.
    plsum = 0

    #variable to store the difference between the value of my current profit/loss row and the value of the previous profit loss row. 
    changes = 0

    #variable to store the value that was in the last row before the next iteration.
    prevrow = 0
    
        
    #this first piece of information I want is the total number of months in the the data set.  Each month is a row in the data set, so I will count each row and return the sum of rows.
    totalmonths = sum(1 for row in csvreader)
   
    # Since the iterating has completed, im using these two lines of code to start again.
    csvfile.seek(0)
    csv_header = next(csvreader)

    #I'm using this line of code to get the sum of the Profit/Loss Column.
    for row in csvreader:
        plsum += (int(row[1]))

#   Since the iterating has completed, im using these two lines of code to start again.
    csvfile.seek(0)
    csv_header = next(csvreader)

    #I'm doing a calculation where I take the current row Profit Loss value minus the previous row profit loss value to get the difference
    #once I get the difference, I'm keeping track of the value that is was in the current row and putting it in the previous row before moving on to the next current row
    for row in csvreader:
        changes = int(row[1]) - prevrow
        prevrow = int(row[1])
        #as these values are being generated, I'm having them entered into a list called pldiff
        pldiff.append(changes)

    #when I check out my pldiff list, I see that the first value is invalid because the differences can only start with the second value in the list.  I'll pop out the first item in this list
    pldiff.pop(0)

    #I'm getting number of values in my list by using the len function to count them.
    diffcount = len(pldiff)

    #next, I want to calculate the average difference.  I'll take list of pldiffs, sum all those values together and then divide by the number of values in my list
    average = (round(sum(pldiff)/diffcount, 2))

    # Here, I'm using my list to figure out the max value in the list 
    maxplpoint = max(pldiff)

    #I want to figure out where in my list this value shows up. I'm using the .index function to do that.  Once I do that I'm going to add 1 to advance to the next row because this value is the difference between two values and I want to attribute it to the value that's higher of the two.
    indexmax = pldiff.index(maxplpoint)+1
    
     #similar to the max, I'm using my list to figure out the min value in the list
    minplpoint = min(pldiff)

     #similar to the max, I'm using my list to figure out the min value in the list
    indexmin = pldiff.index(minplpoint)+1

    #Since the iterating has completed, im using these two lines of code to start again.
    csvfile.seek(0)
    csv_header = next(csvreader)


    #I'm going to iterate over my CSV again to create another list, a list of the values in my dates column
    for row in csvreader:
        pldates.append (row[0])

    #put the date associated with the max index value I found in a variable
    maxdate = pldates[int(indexmax)]

    #put the date associated with the min index value I found in a variable
    mindate = pldates[int(indexmin)]

    #I completed all the tasks.  Here, I'm going to format and print out my results
    print ("Financial Analysis")
    print ("--------------------------------------")
    print ("Total Months: " +str(totalmonths))
    print(f"Total: ${plsum}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: {maxdate}"f" (${maxplpoint})")
    print(f"Greatest Decrease in Profits: {mindate}"f" (${minplpoint})")

    outputpath = os.path.join("bank_report.txt")    
    with open (outputpath, 'w') as report:
        # Now, I'll export the data to a text file
        print ("Financial Analysis", file=report)
        print ("--------------------------------------", file=report)
        print ("Total Months: " +str(totalmonths), file=report)
        print(f"Total: ${plsum}", file=report)
        print(f"Average Change: ${average}", file=report)
        print(f"Greatest Increase in Profits: {maxdate}"f" (${maxplpoint})", file=report)
        print(f"Greatest Decrease in Profits: {mindate}"f" (${minplpoint})", file=report)

    




