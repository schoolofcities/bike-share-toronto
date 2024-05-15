import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

years = [] #a list for the year that trip happened
station_count_by_year = [] #a list for trip count by year
trip_count_by_year = [] #a list for trip count by year
bike_count_by_year = [] #a list for bike count by year
monthly_stats = [] #a list for dataframes that include monthly stats
bikeshareFrames = [] #a list for storing annual bikeshare data
averageDuration = []

#function makes values that are not integer or float into integers, helps getting trip time average. 
def normalize_numbers(number):
    if isinstance(number, int) or isinstance(number, float):
        return number
    else:
        return int(number.replace(',', ''))
"""
within the mainfolder, there are many sub folders that contain excel files containing bikeshare data sometimes the downloaded files contain a further layer of folder, moved excel files out of it. 
"""

mainfolder = "Bikeshare Data" #this folder has many subfolders with excel files in them, sorted by years
folder = os.listdir(mainfolder) #list all the content in mainfolder


for content in folder:
    item = os.path.join(mainfolder, content)
    if os.path.isdir(item): #if the item in the folder is indeed a folder with more excel files
        bikeshare_excel_list = os.listdir(item) #list the excel files

        year = int(item[-4:]) #get year
        """if year != 2020:
            continue"""
        print(year)
        #for each excel file, read the csv and append it to bikeshare_periodically List
        bikeshare_periodically = [] #storing 
        for excel in bikeshare_excel_list:
            excel = os.path.join(mainfolder, content,excel)
            print(excel)
            bikeshare_period_data = pd.read_csv(excel, encoding='latin-1')
            bikeshare_periodically.append(bikeshare_period_data)
        
        bikeshare = pd.concat(bikeshare_periodically) #merge the dataframes of each period of bikeshare data together


        #header has changed since 2019, so have to provide two options 
        if int(year) >= 2019:
            Trip_index = 'Trip Id'
            Trip_Duration = 'Trip  Duration'
            Start_Station_Id ='Start Station Id'
            Start_Time = 'Start Time'
            Start_Station_Name = 'Start Station Name'
            End_Station_Id ='End Station Id'
            End_Time = 'End Time'
            End_Station_Name = 'End Station Name'
            Bike_Id = 'Bike Id'
            User_Type = 'User Type'
        else:
            Trip_index = 'trip_id'
            Trip_Duration = 'trip_duration_seconds'
            Start_Station_Id ='from_station_id'
            Start_Time = 'trip_start_time'
            Start_Station_Name = 'from_station_name'
            End_Station_Id ='to_station_id'
            End_Time = 'to_station_name'
            End_Station_Name = 'to_station_name'
            Bike_Id = 'No Bike Id'
            User_Type = 'user_type'


        #============ Data Cleaning ===========
        
        #print("Cleaning Data")
        
        stations_to_remove = ['Wolfpack', 'PBSC', 'Toronto Bike Shop', 'Make Invisible','Warehouse','Fringe Next Stage - 7219'] #these are not real stations, they were included in data but not really user trips
        bikeshare = bikeshare[~bikeshare[Start_Station_Name].astype(str).str.contains("|".join(stations_to_remove), case=False)]
        bikeshare = bikeshare[~bikeshare[End_Station_Name].astype(str).str.contains("|".join(stations_to_remove), case=False)]
        #drop those trips that last less than 2 minutes and have the same starting and ending station. 
        bikeshare = bikeshare.loc[~((bikeshare[Start_Station_Name] == bikeshare[End_Station_Name]) & (bikeshare[Trip_Duration] < 120))]
        #remove abnormally long trips, here it is defined as those longer than 2hrs
        bikeshare = bikeshare.loc[~(bikeshare[Trip_Duration] > 7200)]
        #separating date and time
        #print("Separating Date and Time")
        
        bikeshare[['StartMonth']] = bikeshare[Start_Time].str.extract(r'^(\d+)\/')
            
        #============Count By Year ===========
        #print("Getting Ridership Count")
        #get ridership count
        #using station ID for analysis because station can change name as it get relocated. 
        """DUE TO DATA LIMITATIONS (BIKESHARE STATIONS HAVE CHANGED LOCATIONS, SOMETIMES EVEN STATION IDS, AND OTHER FACTORS, IT IS MORE MEANINGFUL TO INTERPRET DATA FROM A MONTHLY PERSPECTIVE)"""
        
        #by year, in the form of dataframes
        years.append(year)

        
        #print("Trip Count by year")
        trip_count_by_year.append(len(bikeshare.index)) #counts the ridership each year
        #print("Stations Count by year")
        if year == 2017:
            station_count_by_year.append(bikeshare[Start_Station_Name].nunique())
        else:
            station_count_by_year.append(bikeshare[Start_Station_Id].nunique())
        #print("Average Duration by year")
        averageDuration.append(round(bikeshare[Trip_Duration].mean()/60,2))
        

        #print("Bike Count by year")
        if Bike_Id == 'No Bike Id':
            bike_count_by_year.append('null')
        else: 
            bike_count_by_year.append(bikeshare[Bike_Id].nunique())


        #============ Count by Month ============
        #ridership and station count by month
        #print("Station and Bike Count by Month")
        if year == 2017:
            monthly_count = bikeshare.groupby('StartMonth')[[Start_Station_Name]].nunique().reset_index()
            monthly_count.columns = ['Start Month', 'Station Count']
            monthly_count['Bike Count'] = "null"
                
        else:
            
            if Bike_Id == 'No Bike Id': #some years don't have bike count
                monthly_count = bikeshare.groupby('StartMonth')[[Start_Station_Id]].nunique().reset_index()
                monthly_count.columns = ['Start Month', 'Station Count']
                monthly_count['Bike Count'] = "null"
            else:
                
                monthly_count = bikeshare.groupby('StartMonth')[[Start_Station_Id,Bike_Id]].nunique().reset_index()
                monthly_count.columns = ['Start Month', 'Station Count', 'Bike Count']
                

        monthly_count['Year'] = year #add a new field "year" to the station count dataframe


        #get trip count
        #print("Trip Count by Month")
        count = bikeshare['StartMonth'].value_counts().reset_index()
        count.columns = ["Start Month", "Trip Count"]

        #join the trip count with ridership and station count
        monthly_count = monthly_count.merge(count, on='Start Month')
        #average trip duration
        monthly_average = bikeshare.groupby('StartMonth')[[Trip_Duration]].mean()/60
        monthly_average = monthly_average.reset_index()
        monthly_average.columns = ['Start Month', 'Average Trip Duration']
        
        #join the trip count with ridership and station count
        monthly_count = monthly_count.merge(monthly_average, on='Start Month')
        monthly_stats.append(monthly_count)


#create a dataframe for the ridership by year (ie. 2019 has 200 rides, 2020 has 400 rides)
annual_stats = {"Year": years, "Station Count": station_count_by_year, "Bike Counts": bike_count_by_year, "Trip Count" : trip_count_by_year, 'Average Trip Duration': averageDuration}
annual_stats = pd.DataFrame (annual_stats)


monthly_stats_frame = pd.concat(monthly_stats) #merge the dataframes of each year of bikeshare data together
pd.set_option('display.max_rows', None)

data = []

monthly_stats_frame = monthly_stats_frame.astype({'Start Month':'int'})
monthly_stats_frame = monthly_stats_frame.sort_values(['Year','Start Month']).reset_index().drop(columns='index',axis='1')


for _, row in monthly_stats_frame.iterrows():
    if row['Bike Count'] == "null":
        averageBikeUsage = "null"
    else:
        averageBikeUsage = round(row['Trip Count'] / row['Bike Count'],2)
    data.append({
        "Year": row['Year'],
        "Month": row['Start Month'],
        "YearMonth" : str(row['Year']) + "." + str(row['Start Month']),
        "StationCount" : row['Station Count'],
        "BikeCount" : row['Bike Count'],
        "TripCount" : row['Trip Count'],
        "AverageTripDuration" : round(row['Average Trip Duration'],2),
        "AverageBikeUsage": averageBikeUsage,
        "AverageStationUsage": round(row['Trip Count'] / row['Station Count'],2)
    })