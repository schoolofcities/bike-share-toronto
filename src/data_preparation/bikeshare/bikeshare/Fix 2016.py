import csv 

List2016 = ["Bikeshare Data/bikeshare-ridership-2016/bikeshare-ridership-2016 Q3.csv", "Bikeshare Data/bikeshare-ridership-2016/bikeshare-ridership-2016 Q4.csv"]

for file in List2016:
            
    with open (file) as csvfile:
        bikeReader = csv.reader(csvfile, delimiter = ",", quotechar='|')

        data = []
        i=0
        for row in bikeReader:
            if row[1] == "trip_start_time":
                data.append(row)
                continue
            date = row[1].split(" ") [0]
            time = row[1].split(" ") [1]

            day = date.split("-")[1]
            month = date.split("-")[0]
            year = date.split("-")[2]
            row[1] = str(int(month)) + "/"+ str(int(day)) + "/" + str(int(year)) + " " + time
            data.append(row)

            if row[2] == "trip_end_time":
                continue
            date = row[2].split(" ") [0]
            time = row[2].split(" ") [1]

            day = date.split("-")[1]
            month = date.split("-")[0]
            year = date.split("-")[2]
            row[2] = str(int(month)) + "/"+ str(int(day)) + "/" + str(int(year)) + " " + time
            data.append(row)
            print(i)
            i+=1
        

    with open ("{}-1.csv".format(file.split("/")[2]), 'w', newline='') as csvfile:
        bikeWriter = csv.writer(csvfile, delimiter = ",", quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            bikeWriter.writerow (row)


        
        