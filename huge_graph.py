#make graphs of the results of the number of neighbors testing for all of the models

import csv
import matplotlib.pyplot as plt
import os
import matplotlib.font_manager as fm

#set up font from the file
fpath = os.path.join("Futura.ttf")
prop = fm.FontProperties(fname=fpath)
fname = os.path.split(fpath)[1]

x = []
y = []

with open('results10.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        x.append(int(row["CLASSES"]))
        y.append(float(row["ACCURACY"]))
f.close()

#initilize the graph
fig, ax = plt.subplots(figsize=(20, 10))
ax.set_facecolor('#002b36')

#plot the data
ax.plot(x, y, "o", color="#d33682")

#title and labels
ax.set_title("Accuracy based on Number of Models Used Together".format(fname), fontproperties=prop, size=28)
ax.set_xlabel("Number of Models Used Together".format(fname), fontproperties=prop, size=16)
ax.set_ylabel("Accuracy (%)".format(fname), fontproperties=prop, size=16)

#style axis ticks and numbers
ax.set_yticks(range(40, 61, 1))
ax.set_xticks(range(20, 61, 2))
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(14)
#set limits
ax.set_xlim([15, 65])
ax.set_ylim([40, 60])

#legend
ax.legend(["Model using fire start date, end date, size, location, reporting agency, owner and year"], fontsize=16)


plt.show()
