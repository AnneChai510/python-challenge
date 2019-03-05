import os
import csv

sourceDir = 'CSV_data'
sourceFile = 'CSV_data/budget_data.csv'
filePath = os.path.join(sourceDir,sourceFile)

number_months = 0 
total_amount = 0
greatest_increase_month = ''
greatest_decrease_month = ''
greatest_increase_amount = 0
greatest_decrease_amount = 0
differences = []
prev_amount = 0

# average caculation
def average(avg):
    total = 0
    for item in avg:
        total += item
    return (total/len(avg))

# Open and read csv
with open(filePath, newline="") as fileData:
    csvreader = csv.reader(fileData, delimiter=",")
    next(csvreader,'None')
    for row in csvreader:
        # print(row)
        total_amount += int(row[1])
        number_months += 1 
        differences.append(int(row[1]) - prev_amount)
        prev_amount = int(row[1]) 
        if int(row[1]) > greatest_increase_amount:
            greatest_increase_amount = int(row[1])
            greatest_increase_month = row[0]
        if int(row[1]) < greatest_decrease_amount:
            greatest_decrease_amount = int(row[1])
            greatest_decrease_month = row[0]

differences = differences[1:]



# Out
outputText = []
outputText.append("Financial Analysis")
outputText.append("---------------------------------")
outputText.append("Total Months: " + str(number_months))
outputText.append("Total Revenue: $" + str(total_amount//number_months))
outputText.append("Average Revenue Change: $" + str(round(average(differences),2)))
outputText.append("Greatest Increase in Revenue: " + greatest_increase_month + " ($" + str(greatest_increase_amount) + ")") 
outputText.append("Greatest Decrease in Revenue: " + greatest_decrease_month + " ($" + str(greatest_decrease_amount) + ")")
outputText.append("\n \n \nSource file: " + filePath)


# print 
outputName = input('Please name analysis file: \n')
fileOutput = outputName + '.txt'
with open(fileOutput,'w') as fileOut:
    for line in outputText:
        print(line)
        fileOut.write(line + '\n')







