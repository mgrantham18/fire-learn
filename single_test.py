#MODEL USING START_DOY, END_DOY, SIZE, LAT, LONG, REPORTER, AND OWNER

import csv
from sklearn import neighbors
import numpy as np
import gc

init_fires = []                                      #load up fires into a list
with open('processed3.csv') as f:                    #yes this could be done once but memory constraints
    reader = csv.DictReader(f)
    for row in reader:
        niceRow = []
        niceRow.append(row["CAUSE"])
        niceRow.append(row["START_DOY"])
        niceRow.append(row["END_DOY"])
        niceRow.append(row["SIZE"])
        niceRow.append(row["LAT"])
        niceRow.append(row["LONG"])
        niceRow.append(row["REPORTER"])
        niceRow.append(row["OWNER"])
        niceRow.append(row["YEAR"])
        init_fires.append(niceRow)
print("Read in " + str(len(init_fires)) + " fires.")
f.close()

number_of_neighbors = 1
run_count = 0
while number_of_neighbors < 1000:                       #test knn for k all ints from 1 to 1000
    fires = []
    lefthalf = []
    righthalf = []
    for row in init_fires:                              #scramble the list of fires each time
        if(round(abs(np.random.normal())*100)%2 == 0):  #if random number is even put row in the left half
            lefthalf.append(row)
        else:
            righthalf.append(row)
    for row in lefthalf:                                #concatenate left and right halves
        fires.append(row)
    for row in righthalf:
        fires.append(row)
    print("Scrambled fires")

    limit = 1289936

    targets = []                                        #The causes of fires
    counter = 0
    for row in fires:                                   #Fill list with all the causes from the dataset
        if counter < limit:
            targets.append(row[0])
        else:
            break
        counter+=1
    print(str(len(targets)) + " targets ready.")

    X = []                                              #The start and end DOY, size, and location of a fire
    counter = 0
    for row in fires:                                   #Fill list with the data about fires
        if counter < limit:
            if(row[2] == ""):                           #if end DOY missing assume it is the same as the start
                X.append([int(row[1]), int(row[1]), float(row[3]), float(row[4]), float(row[5]), int(row[6]), int(row[7]), int(row[8])])
            else:
                X.append([int(row[1]), int(row[2]), float(row[3]), float(row[4]), float(row[5]), int(row[6]), int(row[7]), int(row[8])])
        else:
            break
        counter+=1
    print(str(len(X)) + " rows of data ready.")

    target_names = []
    for row in targets:                                 #create list of the names of the causes
        if row not in target_names:
            target_names.append(row)

    target = []                                         #list of targets as ints
    for row in targets:                                 #convert targets to ints based on index in name list
        index = 0
        for name in target_names:
            if(name == row):
                target.append(index)
            index+=1
    print(str(len(target)) + " targets converted to values")
    targets = None
    del targets
    gc.collect()

    knn = neighbors.KNeighborsClassifier(n_neighbors=number_of_neighbors)
    print("K Nearest Neighbors Classifier loaded\nFitting to data...")
    knnfit = knn.fit(X, target)                         #fit the data to the KNN classifier
    print("Classifier fit to data")

    counter = 0
    num_correct = 0
    print("Testing on 100000 rows...")
    for row in fires:                                   #skip to the last 100000 fires and test the model
        if(counter > len(fires)-100000):
            prediction = 0
            if(row[2] != ""):
                prediction = knn.predict([[int(row[1]), int(row[2]), float(row[3]), float(row[4]), float(row[5]), int(row[6]), int(row[7]), int(row[8])]])
            else:
                prediction = knn.predict([[int(row[1]), int(row[1]), float(row[3]), float(row[4]), float(row[5]), int(row[6]), int(row[7]), int(row[8])]])

            if(row[0] == target_names[prediction[0]]):
                num_correct+=1

        counter+=1
    accuracy = num_correct/1000
    print("The model correctly predicted " + str(accuracy) + "% of the test rows")
    file = open('results9.csv', 'a')                     #insert the results into a csv
    line = str(number_of_neighbors) + "," + str(accuracy) + "\n"
    file.write(str(line))
    file.close()

    fires = None
    X = None
    target = None
    target_names = None
    knn = None
    del fires                                           #free up space
    del X
    del target
    del target_names
    del knn
    gc.collect()

    run_count+=1
    #if run_count%5 == 0:
    number_of_neighbors+=1                          #upincrement K
    print("\nCompleted "+str(run_count)+" iterations. Testing model with " + str(number_of_neighbors)+" neighbors")

