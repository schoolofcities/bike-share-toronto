import pandas as pd
import json
import requests
import time
import random

url = "http://localhost:8989/route"

od = pd.read_csv("ridership-data/june2024bikeshareridership-utf8.zip")

print(od)

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

	if random.random() > 0.8:
		xm = (x1 + x2) / 2
		ym = (y1 + y2) / 2
		params = {
			"point": [f"{y1},{x1}", f"{ym},{xm}", f"{y2},{x2}"],
			"profile": "bike",
			"instructions": "false"
		}
	else:
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
	
	if row["Closed Status"] != "TERMINATED":

		if int(row["Start Station Id"]) == int(row["End Station Id"]):

			if row["Start Station Id"] == 7354:
		
				c_options = [[-79.34288,43.61320],[-79.337064,43.622051]]
				r_i = random.randint(0, 1) 
				x_r = c_options[r_i][0]
				y_r = c_options[r_i][1]

				trip = getTrip(row["start_lon"], row["start_lat"], x_r, y_r)

				output.append([int(row["Start Station Id"]), int(row["End Station Id"])] + trip)
			
			elif row["Start Station Id"] in [7016, 7076, 7168]:
		
				c_options = [[-79.389161, 43.612119], [-79.381393, 43.613268], [-79.381114, 43.613299], [-79.379226, 43.614014], [-79.37326, 43.622107], [-79.373217, 43.622371], [-79.375771, 43.616624], [-79.371286, 43.615816], [-79.371243, 43.618597], [-79.371415, 43.618519], [-79.368754, 43.618581], [-79.364162, 43.624608], [-79.365407, 43.62015], [-79.361866, 43.627218], [-79.352403, 43.633539], [-79.354742, 43.633275], [-79.356588, 43.633011], [-79.383581, 43.624717]]

				r_i = random.randint(0, len(c_options) - 1)

				x_r = c_options[r_i][0]
				y_r = c_options[r_i][1]

				trip = getTrip(row["start_lon"], row["start_lat"], x_r, y_r)

				output.append([int(row["Start Station Id"]), int(row["End Station Id"])] + trip)

			elif row["Start Station Id"] in [7658, 7629]:

				trip = getTrip(row["start_lon"], row["start_lat"], -79.502392, -43.65447)

				output.append([int(row["Start Station Id"]), int(row["End Station Id"])] + trip)

			elif row["Start Station Id"] in [7856, 7583]:

				c_options = [[-79.509012,43.66276],[-79.509248,43.662698,]]
				r_i = random.randint(0, 1) 
				x_r = c_options[r_i][0]
				y_r = c_options[r_i][1]

				trip = getTrip(row["start_lon"], row["start_lat"], x_r, y_r)

				output.append([int(row["Start Station Id"]), int(row["End Station Id"])] + trip)

			else:

				x_r = random.random() * 0.01
				y_r = random.random() * 0.01
				
				trip = getTrip(row["start_lon"], row["start_lat"], x_r, y_r)

				output.append([int(row["Start Station Id"]), int(row["End Station Id"])] + trip)

		else:

			trip = getTrip(row["start_lon"], row["start_lat"], row["end_lon"], row["end_lat"])

			output.append([int(row["Start Station Id"]), int(row["End Station Id"])] + trip)
	
	i += 1

	# if i > 100000:
	# 	break
	print(i)

print(time.time() - start_time)

column_names = ["start_id", "end_id", "distance", "duration", "elevation_delta", "polyline_string"]

df = pd.DataFrame(output, columns=column_names)

df.to_csv("ridership-data/trips-graphhopper-output-test.csv", index=False)