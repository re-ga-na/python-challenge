#In this challenge, you are tasked with creating a Python script for analyzing
#the financial records of your company.
#You will give a set of financial data called budget_data.csv.
#The dataset is composed of two columns: Date and Profit/Losses.
#(Thankfully, your company has rather lax standards for accounting so the records are simple.)


#Your task is to create a Python script that analyzes the records to calculate each of the following:
    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #The average of the changes in "Profit/Losses" over the entire period
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period

#importing libraries
import os
import csv

#path to feed in csv data
csvpath = os.path.join("budget_data.csv")

#setting variables and make empty lists. 
months = 1
total = 0
net_change = 0
maxloss = ["", 99999999999]
maxprofit = ["", 0]

profit = []
readerdata = []

#reading thru csv data
with open(csvpath) as budget_data:
    reader = csv.reader(budget_data, delimiter = ',')
    #skipping the header row
    header = next(reader)

    row1 = next(reader)
    previousrow = int(row1[1])
    total = int(row1[1])

#collects stats for each month
    for readerdata in reader:
        months = months + 1
        total = total + int(readerdata[1])
        net_change = int(readerdata[1]) - previousrow
        profit.append(net_change)
        previousrow = int(readerdata[1])

#finds the highest profits and losses
        if (net_change > maxprofit[1]):
            maxprofit[0] = readerdata[0]
            maxprofit[1] = net_change
        elif (net_change < maxloss[1]):
            maxloss[0] = readerdata[0]
            maxloss[1] = net_change

#calculates avg change
    averagechange = sum(profit)/len(profit)

#creates path for output
outputpath = os.path.join("financialanalysis.txt")

financialanalysis = (
    f"---------------------------------"
    f"\nFinancial Analysis"
    f"\n---------------------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${total}\n"
    f"Average  Change: ${round(averagechange,2)}\n"
    f"Greatest Increase in Profits: {maxprofit[0]} (${maxprofit[1]})\n"
    f"Greatest Decrease in Profits: {maxloss[0]} (${maxloss[1]})\n"
    f"---------------------------------"    
    )

print(financialanalysis)

#writes textfile of output
with open(outputpath, "w") as txt_file:
     txt_file.write(financialanalysis)

