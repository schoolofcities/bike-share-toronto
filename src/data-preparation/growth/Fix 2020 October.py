import csv 

"""
TripID         Duration        Trip Start Time     Start Station Name      
01234567       156             mm/dd/yyyyy         A Station               --> normal data
01234568       1350            mm/dd/yyyyy         B Station               --> normal data
01234569       1563            mm/dd/yyyyy         C Station               --> normal data
01234570       178             mm/dd/yyyyy         D Station               --> normal data
01234571156    mm/dd/yyyyy     D Station                                   --> irregular data
012345721683   mm/dd/yyyyy     D Station                                   --> irregular data

"""
with open ("Bikeshare Data/bikeshare-ridership-2020/2020-10.csv",newline='', encoding='latin-1') as csvfile:
    bikeReader = csv.reader(csvfile, delimiter = ",", quotechar='|')

    data = []
    for row in bikeReader:

        if len(row[2].split("/")) >1: # find rows where the trip start time is in the duration field
            durationDigits = len(row[0])-8  #grab the first 8 digit
            duration = int(row[0]) - int(row[0][0:8])*10**durationDigits #remove the first 8 digits, you have the trip duration
            row[0] = row[0][0:8] #row[0] is trip ID, which is the first 8 digit
            row.insert(1, duration)
            data.append(row)

        else: 
            data.append(row)

#export to a new spreadsheet. 
with open ("Bikeshare Data/bikeshare-ridership-2020/2020-10.csv", 'w', newline='', encoding='latin-1') as csvfile:
    bikeWriter = csv.writer(csvfile, delimiter = ",", quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in data:
        bikeWriter.writerow (row)
        