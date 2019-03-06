import os
import csv

sourceDir = 'CSV_data'
sourceFile = 'CSV_data/election_data.csv'
filePath = os.path.join(sourceDir,sourceFile)


# open file 
# Initialize variables to track
voters = []
candidates = {}
num_votes = 0


with open(filePath,'r',newline='') as fileData:
    csvreader = csv.reader(fileData,delimiter=',')
    next(csvreader,'None') 
    for row in csvreader:
        # print(row)
            if row[2] not in candidates.keys():
                candidates[row[2]] = 1
            else:
                candidates[row[2]] += 1
            num_votes += 1
        

# calculate the winner
winner = max(candidates, key=candidates.get)


# Create output string
lineBreak = '--------------------------------------'
outputText = []
outputText.append('Election Results')
outputText.append(lineBreak)
outputText.append('Total Votes: ' + str(nVotes))
outputText.append(lineBreak)
for k,v in candidates.items():
    outputText.append(k + ': ' + str(round((100*v/nVotes),2)) + '% (' + str(v) + ')')
outputText.append(lineBreak)
outputText.append('Winner: ' + winner)
outputText.append(lineBreak)
outputText.append('\n\n\nSource file: ' + filePath)


# print to terminal and text file
outputName = input('Please name analysis file: \n')
fileOutput = outputName + '.txt'
with open(fileOutput,'w') as fileOut:
    for line in outputText:
        print(line)
        fileOut.write(line + '\n')
