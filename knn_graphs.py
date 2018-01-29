#make graphs of the results of the number of neighbors testing for all of the models

import csv
import matplotlib.pyplot as plt
import os
import matplotlib.font_manager as fm

#set up font from the file
fpath = os.path.join("Futura.ttf")
prop = fm.FontProperties(fname=fpath)
fname = os.path.split(fpath)[1]


x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []
x5 = []
y5 = []


#load in 500 rows of data from each. Some contain more rows than that, but due to time constraints more could not be run on all
length = 500
count = 0
with open('results9.csv') as f:         #Start DOY, End DOY, Size, Lat, Long, Owner, Reporting agency, Year
    reader = csv.DictReader(f)
    for row in reader:
        if(count <= length):
            x5.append(int(row["NEIGHBORS"]))
            y5.append(float(row["ACCURACY"]))
        count+=1
f.close()

count = 0
with open('results7.csv') as f:         #Start DOY, End DOY, Size, Lat, Long, Owner, Reporting agency
    reader = csv.DictReader(f)
    for row in reader:
        if(count <= length):
            x4.append(int(row["NEIGHBORS"]))
            y4.append(float(row["ACCURACY"]))
        count+=1
f.close()

count = 0
with open('results5.csv') as f:         #Start DOY, End DOY, Size, Lat, Long, Owner
    reader = csv.DictReader(f)
    for row in reader:
        if(count <= length):
            x3.append(int(row["NEIGHBORS"]))
            y3.append(float(row["ACCURACY"]))
        count+=1
f.close()

count = 0
with open('results3.csv') as f:             #Start DOY, End DOY, Size, Lat, Long, and Year
    reader = csv.DictReader(f)
    for row in reader:
        if(count <= length):
            x2.append(int(row["NEIGHBORS"]))
            y2.append(float(row["ACCURACY"]))
        count+=1
f.close()

count = 0
with open('results.csv') as f:              #Start DOY, End DOY, Size, Lat, Long
    reader = csv.DictReader(f)
    for row in reader:
        if(count <= length):
            x1.append(int(row["NEIGHBORS"]))
            y1.append(float(row["ACCURACY"]))
        count+=1
f.close()


#initilize the graph
fig, ax = plt.subplots(figsize=(20, 10))
ax.set_facecolor('#002b36')

#plot the data
ax.plot(x1, y1, "o", color="#cb4b16")
#ax.plot(x2, y2, "o", color="red")
ax.plot(x3, y3, "o", color="#859900")
ax.plot(x4, y4, "o", color="#2aa198")
ax.plot(x5, y5, "o", color="#d33682")

#title and labels
ax.set_title("K Nearest Neighbors Accuracy".format(fname), fontproperties=prop, size=28)
ax.set_xlabel("Number of Neighbors (K)".format(fname), fontproperties=prop, size=16)
ax.set_ylabel("Accuracy (%)".format(fname), fontproperties=prop, size=16)

#style axis ticks and numbers
ax.set_yticks(range(40, 61, 1))
ax.set_xticks(range(0, length+6, 100))
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(14)
#set limits
ax.set_xlim([-5, length+5])
ax.set_ylim([40, 60])

#legend
ax.legend(["Model using fire start date, end date, size, and location", "Model using fire start date, end date, size, location, and owner", "Model using fire start date, end date, size, location, owner, and reporting agency", "Model using fire start date, end date, size, location, owner, reporting agency, and year"], fontsize=16)


plt.show()

