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
		points = [
			[
			x1, y1
			],
			[
			xm, ym
			],
			[
			x2, y2
			]
		]
	else:
		points = [
			[
			x1, y1
			],
			[
			x2, y2
			]
		]

	params = {
		"points": points,
		"profile": "bike",
		"ch.disable": True,
		"custom_model": {
			"priority": [
				{
					"if": "road_class == PRIMARY",
					"multiply_by": 0.8
				},
				{
					"if": "road_class == CYCLEWAY",
					"multiply_by": 1.5
				},
				{
					"if": "in_custom1",
					"multiply_by": 0.01
				},
				{
					"if": "in_custom2",
					"multiply_by": 0.01
				},
				{
					"if": "in_custom3",
					"multiply_by": 0
				},
				{
					"if": "in_custom4",
					"multiply_by": 0
				}
			],
			"areas": {
				"custom1": {
					"type": "Feature",
					"id": "something",
					"properties": {},
					"geometry": {
						"type": "Polygon",
						"coordinates": [
							[
								[
								-79.35322130473351,
								43.65671846016616
								],
								[
								-79.35322130473351,
								43.65649270861002
								],
								[
								-79.35268955146468,
								43.65649270861002
								],
								[
								-79.35268955146468,
								43.65671846016616
								],
								[
								-79.35322130473351,
								43.65671846016616
								]
							]
						]
					}
				},
				"custom2": {
					"type": "Feature",
					"id": "something",
					"properties": {},
					"geometry": {
						"type": "Polygon",
						"coordinates": [
							[
								[
								-79.35446680540271,
								43.64930207313603
								],
								[
								-79.34808167180002,
								43.64930207313603
								],
								[
								-79.34808167180002,
								43.6516276036497
								],
								[
								-79.35446680540271,
								43.6516276036497
								],
								[
								-79.35446680540271,
								43.64930207313603
								]
							]
						]
					}
				},
				"custom3": {
					"type": "Feature",
					"id": "something",
					"properties": {},
					"geometry": {
						"type": "Polygon",
						"coordinates": [
							[
								[
								-79.41172834841538,
								43.62639572070586
								],
								[
								-79.41172834841538,
								43.62976681506831
								],
								[
								-79.4228208491374,
								43.62976681506831
								],
								[
								-79.4228208491374,
								43.62639572070586
								],
								[
								-79.41172834841538,
								43.62639572070586
								]
							]
						]
					}
				},
				"custom4": {
					"type": "Feature",
					"id": "something",
					"properties": {},
					"geometry": {
						"type": "Polygon",
						"coordinates": [
							[
								[
								-79.39762819338937,
								43.63327139326614
								],
								[
								-79.39762819338937,
								43.630661389644445
								],
								[
								-79.3931457241289,
								43.630661389644445
								],
								[
								-79.3931457241289,
								43.63327139326614
								],
								[
								-79.39762819338937,
								43.63327139326614
								]
							]
						]
					}
				}
			}
		}
	} 

	try:
		headers = {
			"Content-Type": "application/json"
		}
		response = requests.post(url, headers=headers, data=json.dumps(params))
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
				
				r_t = random.random()

				if r_t < 0.66:
					c_options = [[-79.34288,43.61320],[-79.337064,43.622051]]
					r_i = random.randint(0, 1) 
					x_r = c_options[r_i][0]
					y_r = c_options[r_i][1]

				else: 

					c_options = [[-79.327053, 43.617622], [-79.324006, 43.617498], [-79.327268, 43.618896], [-79.335207, 43.619362], [-79.34334, 43.613649], [-79.343061, 43.618791], [-79.322461, 43.622481], [-79.343699,43.613259], [-79.344013, 43.61336], [-79.340284, 43.616618], [-79.340247, 43.616665], [-79.322394, 43.626016], [-79.321493, 43.633285]]

					r_i = random.randint(0, len(c_options) - 1)

					x_r = c_options[r_i][0]
					y_r = c_options[r_i][1]


				trip = getTrip(row["start_lon"], row["start_lat"], x_r, y_r)

				output.append([int(row["Start Station Id"]), int(row["End Station Id"])] + trip)
			
			elif row["Start Station Id"] in [7016, 7076, 7168]:
		
				# c_options = [[-79.389161, 43.612119], [-79.381393, 43.613268], [-79.381114, 43.613299], [-79.379226, 43.614014], [-79.37326, 43.622107], [-79.373217, 43.622371], [-79.375771, 43.616624], [-79.371286, 43.615816], [-79.371243, 43.618597], [-79.371415, 43.618519], [-79.368754, 43.618581], [-79.364162, 43.624608], [-79.365407, 43.62015], [-79.361866, 43.627218], [-79.352403, 43.633539], [-79.354742, 43.633275], [-79.356588, 43.633011], [-79.383581, 43.624717],[-79.389711, 43.613661], [-79.375785, 43.616628], [-79.371772, 43.619851], [-79.373296, 43.621529], [-79.390033, 43.61528], [-79.390033, 43.615284], [-79.371143, 43.615642], [43.615642,-79.375317]]

				# r_i = random.randint(0, len(c_options) - 1)

				# x_r = c_options[r_i][0]
				# y_r = c_options[r_i][1]

				x_r = -79.391356 + random.random() * ((-79.349543) - (-79.391356))
				y_r = 43.610711 + random.random() * (43.634325 - 43.610711)


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

				x_r = row["start_lon"] + random.random() * 0.05 - random.random() * 0.05
				y_r = row["start_lat"] + random.random() * 0.05 - random.random() * 0.05
				
				trip = getTrip(row["start_lon"], row["start_lat"], x_r, y_r)

				output.append([int(row["Start Station Id"]), int(row["End Station Id"])] + trip)

		else:

			trip = getTrip(row["start_lon"], row["start_lat"], row["end_lon"], row["end_lat"])

			output.append([int(row["Start Station Id"]), int(row["End Station Id"])] + trip)
	
	i += 1

	# if i > 10000:
	# 	break
	print(i)

print(time.time() - start_time)

column_names = ["start_id", "end_id", "distance", "duration", "elevation_delta", "polyline_string"]

df = pd.DataFrame(output, columns=column_names)

df.to_csv("ridership-data/trips-graphhopper-output-all.csv", index=False)