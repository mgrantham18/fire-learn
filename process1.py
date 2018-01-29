import csv
import requests
import json
fires = []

with open('fire.csv') as f:
    reader = csv.DictReader(f)
    counter = 0
    f = open('processed.csv', 'a')
    for row in reader:
        if(row["STAT_CAUSE_DESCR"] != "Miscellaneous" and row["STAT_CAUSE_DESCR"] != "Missing/Undefined" and row["DISCOVERY_DOY"] != "" and row["FIRE_SIZE"] != "" and row["LATITUDE"] != "" and row["LONGITUDE"] != ""):
            if counter > 0:
                fire = []
                fire.append(row["STAT_CAUSE_DESCR"])
                fire.append(row["DISCOVERY_DOY"])
                fire.append(row["CONT_DOY"])
                fire.append(row["FIRE_SIZE"])
                fire.append(row["LATITUDE"])
                fire.append(row["LONGITUDE"])
                fire.append(row["NWCG_REPORTING_AGENCY"])
                fire.append(row["FIRE_YEAR"])
                fire.append(row["OWNER_DESCR"])
                # url = 'http://data.fcc.gov/api/block/find?format=json&latitude=' + row["LATITUDE"] + '&longitude=' + row["LONGITUDE"] + '&showall=true'
                # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
                # result = requests.get(url, headers=headers)
                # parsed = (result.content.decode())
                # data = json.loads(parsed)
                # fire.append(data["State"]["name"])
                # fire.append(data["County"]["name"])
                fires.append(fire)
                line = str(fire[0]) + "," + str(fire[1]) + "," + str(fire[2]) + "," + str(fire[3]) + "," + str(fire[4]) + "," + str(fire[5]) + "," + str(fire[6]) + "," + str(fire[7]) + "," + str(fire[8]) + "\n"
                f.write(str(line))
            #print(fire)
            counter+=1
        if(counter%100 == 0):
            print(counter)


