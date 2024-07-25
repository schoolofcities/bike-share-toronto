import json
import requests

url = "http://localhost:8989/route"

params = {
	"points": [
		[
		-79.173858, 43.779876
		],
		[
		-79.19372, 43.778053,
		]
	],
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
				"if": "in_custom2",
				"multiply_by": 0.01
			},
			{
				"if": "in_custom2",
				"multiply_by": 0.01
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
			}
		}
	}
	} 

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=json.dumps(params))
response.raise_for_status() 
data = response.json()

print(json.dumps(data, indent=4))