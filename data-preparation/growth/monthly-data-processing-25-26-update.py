import pandas as pd
import os
import json

data = []

for filename in sorted(os.listdir("ridership-data-25-26")):
	if filename.endswith('.csv'):
		file_path = os.path.join("ridership-data-25-26", filename)

		print(file_path)

		df = pd.read_csv(file_path, encoding='utf-8',encoding_errors = 'replace')

		df = df.loc[~((df["Start_Station_Id"] == df["End_Station_Id"]) & (df["Trip_Duration"] < 120))]

		df['date'] = pd.to_datetime(df['Start_Time'], errors='coerce')
		first_row_date = df['date'].iloc[0]

		if pd.isna(first_row_date):
			continue

		Year = first_row_date.year
		Month = first_row_date.month
		YearMonth = str(Year) + ";" + str(Month)
		StationCount = df['Start_Station_Id'].nunique()
		BikeCount = df['Bike_Id'].nunique()
		TripCount = len(df)
		AverageTripDuration = round(df['Trip_Duration'].mean() / 60, 2)
		AverageBikeUsage = round(TripCount / BikeCount, 2)
		AverageStationUsage = round(TripCount / StationCount, 2)

		data.append(
			{
				"Year": int(Year),
				"Month": int(Month),
				"YearMonth": YearMonth,
				"StationCount": int(StationCount),
				"BikeCount": int(BikeCount),
				"TripCount": int(TripCount),
				"AverageTripDuration": float(AverageTripDuration),
				"AverageBikeUsage": float(AverageBikeUsage),
				"AverageStationUsage": float(AverageStationUsage)
			}
		)

print(data)

with open("data-update-25-26.json", 'w') as json_file:
    json.dump(data, json_file, indent='\t')