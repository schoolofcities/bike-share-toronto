import csv 

with open ("Bikeshare Data/bikeshare-ridership-2017/Bikeshare Ridership (2017 Q1).csv") as csvfile:
    bikeReader = csv.reader(csvfile, delimiter = ",", quotechar='|')

    data = []
    for row in bikeReader:
        if row[1] == "trip_start_time":
            data.append(row)
            continue
        date = row[1].split(" ") [0]
        time = row[1].split(" ") [1]

        day = date.split("/")[0]
        month = date.split("/")[1]
        year = date.split("/")[2]
        row[1] = str(int(month)) + "/"+ str(int(day)) + "/" + str(int(year)) + " " + time
        data.append(row)
        if row[2] == "trip_end_time":
            continue
        date = row[2].split(" ") [0]
        time = row[2].split(" ") [1]

        day = date.split("/")[0]
        month = date.split("/")[1]
        year = date.split("/")[2]
        row[2] = str(int(month)) + "/"+ str(int(day)) + "/" + str(int(year)) + " " + time
        data.append(row)

with open ("Bikeshare Data/bikeshare-ridership-2017/Bikeshare Ridership (2017 Q1)-1 .csv", 'w', newline='') as csvfile:
    bikeWriter = csv.writer(csvfile, delimiter = ",", quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in data:
        bikeWriter.writerow (row)


        
        