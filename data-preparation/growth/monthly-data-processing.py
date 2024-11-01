import pandas as pd
import os
import json

data = []

for filename in sorted(os.listdir("ridership-data")):
	if filename.endswith('.csv'):
		file_path = os.path.join("ridership-data", filename)

		print(file_path)

		df = pd.read_csv(file_path, encoding='utf-8',encoding_errors = 'replace')

		df = df.loc[~((df["Start Station Id"] == df["End Station Id"]) & (df["Trip  Duration"] < 120))]

		df['date'] = pd.to_datetime(df['Start Time'], errors='coerce', format="%m/%d/%Y %H:%M")
		first_row_date = df['date'].iloc[0]

		Year = first_row_date.year
		Month = first_row_date.month
		YearMonth = str(Year) + ";" + str(Month)
		StationCount = df['Start Station Id'].nunique()
		BikeCount = df['Bike Id'].nunique()
		TripCount = len(df)
		AverageTripDuration = round(df['Trip  Duration'].mean() / 60, 2)
		AverageBikeUsage = round(TripCount / BikeCount, 2)
		AverageStationUsage = round(TripCount / StationCount, 2)

		data.append(
			{
				"Year": Year,
				"Month": Month,
				"YearMonth": YearMonth,
				"StationCount": StationCount,
				"BikeCount": BikeCount,
				"TripCount": TripCount,
				"AverageTripDuration": AverageTripDuration,
				"AverageBikeUsage": AverageBikeUsage,
				"AverageStationUsage": AverageStationUsage
			}
		)

print(data)

with open("data-update.json", 'w') as json_file:
    json.dump(data, json_file, indent='\t')