#make graphs of the frequency distribution from the multi model tests

import csv
import matplotlib.pyplot as plt
import os
import matplotlib.font_manager as fm

#init plot
fig, ax = plt.subplots(figsize=(20, 10))
ax.set_facecolor('#002b36')

#set up font
fpath = os.path.join("Futura.ttf")
prop = fm.FontProperties(fname=fpath)
fname = os.path.split(fpath)[1]

#define files to load in, set the colors and legend labels
files = ["results2.csv", "results4.csv", "results6.csv", "results8.csv"]
names = ["Model: Start Day, End Day, Size, Latitude, and Longitude", "Model w/ Owner", "Model w/ Owner and Reporting Agency", "Model w/ Owner, Reporting Agency, and Year"]
colors = ["#cb4b16", "#859900", "#2aa198", "#d33682"]
count = 0
for file in files:
    data = []
    i = 1
    while i <= 60:
        data.append([i,0,0]) #number, total, total got right
        i+=1
    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            data[int(row[0])-1][1] += 1
            if(int(row[1]) == 1):
                data[int(row[0])-1][2] += 1

    #set up x values and move them so the bars dont overlap
    X = []
    for row in data:
        if(row[1] == 0 or row[0] < 24):
            continue
        else:
            offset = -0.4
            if(count == 1):
                offset = -0.2
            elif(count == 2):
                offset = 0
            elif(count == 3):
                offset = 0.2
            X.append(row[0]+offset)

    y = []
    for row in data:
        if(row[1] == 0 or row[0] < 24):
            continue
        else:
            y.append(row[1])

    ax.bar(X, y, color=colors[count], width=0.2, align='edge', alpha=1)

    count+=1

ax.legend(names, fontsize=16)
ax.set_xlim([23, 61])
ax.set_ylim([0, 80000])
ax.set_title("Number of K Nearest Neighbor Models in Agreement Frequency".format(fname), fontproperties=prop, size=28)
ax.set_xlabel("Number of Models in Agreement".format(fname), fontproperties=prop, size=16)
ax.set_ylabel("Frequncy".format(fname), fontproperties=prop, size=16)
ax.set_yticks(range(0, 80001, 5000))
ax.set_xticks(range(24, 61, 1))
#format labels
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(14)
plt.show()
