import pandas as pd
import os
import json

data = []

csv_files = [f for f in sorted(os.listdir("ridership-data-24")) if f.endswith('.csv')]
if not csv_files:
    raise SystemExit("No CSV files found in ridership-data-24")

frames = []
for filename in csv_files:
    file_path = os.path.join("ridership-data-24", filename)
    print(file_path)
    df = pd.read_csv(file_path, encoding='utf-8', encoding_errors='replace')
    frames.append(df)

df = pd.concat(frames, ignore_index=True)

df = df.loc[~((df["Start_Station_Id"] == df["End_Station_Id"]) & (pd.to_numeric(df["Trip_Duration"], errors='coerce') < 120))]

df['date'] = pd.to_datetime(df['Start_Time'], errors='coerce')
df['Year'] = df['date'].dt.year
df['Month'] = df['date'].dt.month

df = df.dropna(subset=['date'])

for (Year, Month), group in df.groupby(['Year', 'Month'], sort=True):
    YearMonth = f"{Year};{Month}"
    StationCount = group['Start_Station_Id'].nunique()
    BikeCount = group['Bike_Id'].nunique()
    TripCount = len(group)
    AverageTripDuration = round(pd.to_numeric(group['Trip_Duration'], errors='coerce').mean() / 60, 2)
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

with open("data-update-24.json", 'w') as json_file:
    json.dump(data, json_file, indent='\t')
