import csv
from sklearn import neighbors
import numpy as np
import gc

def mode(list):
    freqlist = []
    for i in list:
        if i not in freqlist:
            freqlist.append(i)

    freq = [0] * len(freqlist)
    for i in list:
        freqindex = freqlist.index(i)
        freq[freqindex]+=1

    dictionary = {}
    counter = 0
    for i in freqlist:
        dictionary[i] = freq[counter]
        counter+=1

    highest = max(dictionary.values())

    modes = ([k for k, v in dictionary.items() if v == highest])
    return(modes)



init_fires = []                                     #load up fires into a list
with open('processed2.csv') as f:                    #yes this could be done once but memory constraints
    reader = csv.DictReader(f)
    for row in reader:
        niceRow = []
        niceRow.append(row["CAUSE"])
        niceRow.append(row["START_DOY"])
        niceRow.append(row["END_DOY"])
        niceRow.append(row["SIZE"])
        niceRow.append(row["LAT"])
        niceRow.append(row["LONG"])
        init_fires.append(niceRow)
print("Read in " + str(len(init_fires)) + " fires.")
f.close()

number_of_neighbors = [35, 10, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 60, 61, 62, 63, 65, 66, 67, 69, 70, 72, 76, 83, 84, 87, 99]

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

lefthalf = None
righthalf = None                                    #delete these to save some memory
del lefthalf
del righthalf
gc.collect()

limit = 1289936                                     #number to limit learning model by

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
            X.append([int(row[1]), int(row[1]), float(row[3]), float(row[4]), float(row[5])])
        else:
            X.append([int(row[1]), int(row[2]), float(row[3]), float(row[4]), float(row[5])])
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

knn_class = []
knnfit = []
knn_counter = 0
for non in number_of_neighbors:
    knn_class.append(neighbors.KNeighborsClassifier(n_neighbors=non))
    print("K Nearest Neighbors Classifier loaded for " + str(non) + " neighbors\n" + str(knn_counter) + "/60")
    knnfit.append(knn_class[knn_counter].fit(X, target))  #fit the data to the KNN classifier
    #print(str(non) +" Nearest Neighbors Classifier fit to data")
    knn_counter+=1

counter = 0
num_correct = 0
print("Testing on 100000 rows...")
for row in fires:                                   #skip to the last 100000 fires and test the model
    if(counter > len(fires)-39966): #60034
        if(counter%100 == 0):
            print("Currently tested " + str((len(fires)-39966)-counter) + " rows.")
        prediction = []
        if(row[2] != ""):
            for knn in knn_class:
                prediction.append(knn.predict([[int(row[1]), int(row[2]), float(row[3]), float(row[4]), float(row[5])]])[0])
        else:
            for knn in knn_class:
                prediction.append(knn.predict([[int(row[1]), int(row[1]), float(row[3]), float(row[4]), float(row[5])]])[0])
        #print(prediction)
        solution = mode(prediction)
        while(len(solution) > 1):
            del prediction[1]
            solution = mode(prediction)

        if(row[0] == target_names[solution[0]]):
            file = open('results2.csv', 'a')
            line = str(prediction.count(mode(prediction))) + ",1\n"
            file.write(str(line))
            file.close()
        else:
            file = open('results2.csv', 'a')
            line = str(prediction.count(mode(prediction))) + ",0\n"
            file.write(str(line))
            file.close()
        #printProgressBar(counter-(len(fires)-100000), 100000, prefix = 'Testing:', suffix = 'Complete', length = 50)
    counter+=1
print("Complete")
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


