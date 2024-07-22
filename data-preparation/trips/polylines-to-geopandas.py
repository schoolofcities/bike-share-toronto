import pandas as pd
import geopandas as gpd
from shapely.geometry import LineString
import polyline

def decode_polyline(encoded_polyline):
	try:
		coordinates = polyline.decode(encoded_polyline)
		return LineString(coordinates)
	except:
		return None

df = pd.read_csv("trips-graphhopper-output.csv").head(25)

print(df)

df['geometry'] = df['polyline_string'].apply(decode_polyline)

print(df)
