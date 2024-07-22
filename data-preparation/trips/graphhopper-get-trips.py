import pandas as pd
import json
import requests
import time

url = "http://localhost:8989/route"

od = pd.read_csv("origin-destination-trip-counts-all.csv")

with open("station-information-july112024.json", "r") as json_file:	
	stations = pd.DataFrame(json.load(json_file)["data"]["stations"])
	stations = stations[["station_id","lon","lat"]]
	stations['station_id'] = stations['station_id'].astype(int)

od = od.merge(stations, left_on='Start Station Id', right_on="station_id", how='left')
od = od.rename(columns={'lat': 'start_lat', 'lon': 'start_lon'})
del od["station_id"]
od = od.merge(stations, left_on='End Station Id', right_on="station_id", how='left')
od = od.rename(columns={'lat': 'end_lat', 'lon': 'end_lon'})
del od["station_id"]

print(od)




def getTrip(x1, y1, x2, y2):

	params = {
		"point": [f"{y1},{x1}", f"{y2},{x2}"],
		"profile": "bike",
		"instructions": "false"
	}

	try:
		response = requests.get(url, params=params)
		response.raise_for_status() 
		data = response.json()
		data = data['paths'][0]
		distance = data['distance']
		duration = data['time']
		elevation_delta = data['ascend'] - data['descend']
		polyline_string = data['points']
		
	except requests.RequestException as e:
		distance = 0
		duration = 0
		elevation_delta = 0
		polyline_string = "NA"

	
	return [distance, duration, elevation_delta, polyline_string]



start_time = time.time()

i = 0
output = []

for index, row in od.iterrows():
    
	trip = getTrip(row["start_lon"], row["start_lat"], row["end_lon"], row["end_lat"])

	output.append([int(row["Start Station Id"]), int(row["End Station Id"])] + trip)

	i += 1
	print(i)

print(time.time() - start_time)

column_names = ["start_id", "end_id", "distance", "duration", "elevation_delta", "polyline_string"]

df = pd.DataFrame(output, columns=column_names)

df.to_csv("ridership-data/trips-graphhopper-output.csv", index=False)