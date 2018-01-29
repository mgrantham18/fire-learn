import csv
import numpy as np

init_fires = []                                     #load up fires into a list
with open('processed.csv') as f:                    #yes this could be done once but memory constraints
    reader = csv.DictReader(f)
    for row in reader:
        niceRow = []
        niceRow.append(row["CAUSE"])
        niceRow.append(row["START_DOY"])
        niceRow.append(row["END_DOY"])
        niceRow.append(row["SIZE"])
        niceRow.append(row["LAT"])
        niceRow.append(row["LONG"])
        niceRow.append(row["YEAR"])
        niceRow.append(row["OWNER"])
        init_fires.append(niceRow)
print("Read in " + str(len(init_fires)) + " fires.")
f.close()

owners = []
for row in init_fires:                                 #create list of the names of the causes
    if row[8] not in owners:
        owners.append(row[8])
        print(row)
fires = []                                         #list of targets as ints
for row in init_fires:                                 #convert targets to ints based on index in name list
    new_row = []
    new_row.append(row[0])
    new_row.append(row[1])
    new_row.append(row[2])
    new_row.append(row[3])
    new_row.append(row[4])
    new_row.append(row[5])
    new_row.append(row[6])
    new_row.append(owners.index(row[7]))
    fires.append(new_row)

#print(init_fires)
#print(owners)
#print(fires)
f = open('processed2.csv', 'a')
for row in fires:
    line = str(row[0]) + "," + str(row[1]) + "," + str(row[2]) + "," + str(row[3]) + "," + str(row[4]) + "," + str(row[5]) + "," + str(row[6]) + "," + str(row[7]) +"\n"
    f.write(str(line))
f.close()
