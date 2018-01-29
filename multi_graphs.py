import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import sys
import os
import matplotlib.font_manager as fm


fig, ax = plt.subplots(figsize=(20, 10))
ax.set_facecolor('#002b36')

fpath = os.path.join("Futura.ttf")
prop = fm.FontProperties(fname=fpath)
fname = os.path.split(fpath)[1]

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

    #print(data)
    sum = 0
    total = 0
    for row in data:
        sum += row[2]
        total += row[1]
    print("total accuracy " + names[count] + ": " + str(sum/total*100))

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
    print(X)
    y = []
    for row in data:
        if(row[1] == 0 or row[0] < 24):
            continue
        else:
            y.append(row[2]/row[1]*100)
    err = []
    for row in data:
        if(row[1] == 0 or row[0] < 24):
            continue
        else:
            values = []
            i = 0
            while i < row[1]*(row[2]/100):
                values.append(1)
                i+=1
            while len(values) < row[1]:
                values.append(0)
            err.append(stats.sem(values)*100)

    # c = 0
    # for e in y:                                               # remove any bars whose error goes below 0
    #     if e-err[c] < 1:
    #         X.pop(c)
    #         err.pop(c)
    #         y.pop(c)
    #     c+=1

    ax.bar(X, y, color=colors[count], width=0.2, align='edge', alpha=1)

    x = []
    for i in X:
        x.append(i+0.1)

    (_, caps, _) = ax.errorbar(x, y, yerr=err, color='#93a1a1', linestyle='None', label='_nolegend_', capsize=0.2, capthick=0.2)
    for cap in caps:
        cap.set_color(colors[count])

    count+=1

ax.legend(names, fontsize=16)
ax.set_xlim([23, 61])
ax.set_ylim([0, 80])
ax.set_title("Number of K Nearest Neighbor Models in Agreement vs. Accuracy".format(fname), fontproperties=prop, size=28)
ax.set_xlabel("Number of Models in Agreement".format(fname), fontproperties=prop, size=16)
ax.set_ylabel("Accuracy (%)".format(fname), fontproperties=prop, size=16)
ax.set_yticks(range(0, 81, 5))
ax.set_xticks(range(24, 61, 1))
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(14)
plt.show()
