import json

# Read JSON data from a file
with open('station-information-july112024.json', 'r') as f:
	data = json.load(f)

# Convert the data to GeoJSON format
geojson = {
	"type": "FeatureCollection",
	"features": []
}

for station in data["data"]["stations"]:
	feature = {
		"type": "Feature",
		"geometry": {
			"type": "Point",
			"coordinates": [station['lon'], station['lat']]
		},
		"properties": {
			"station_id": station['station_id']
		}
	}
	geojson["features"].append(feature)

# Save the GeoJSON to a file
with open('station-information-july112024.geojson', 'w') as f:
	json.dump(geojson, f, indent=2)
