import pandas as pd
import geopandas as gpd
from shapely.geometry import LineString
import polyline
import random

def decode_polyline(encoded_polyline):

	try:
		coordinates = polyline.decode(encoded_polyline)
		coordinates = [(lon + 0.0002 * random.random() ** 3 - + 0.0002 * random.random() ** 3, lat + 0.0002 * random.random() ** 3 - + 0.0002 * random.random() ** 3) for lat, lon in coordinates]
		return LineString(coordinates)
	except:
		return None

df = pd.read_csv("ridership-data/trips-graphhopper-output-test.csv")


df['geometry'] = df['polyline_string'].apply(decode_polyline)

df = gpd.GeoDataFrame(df, geometry='geometry')

df.crs = "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs"

df.to_file("trips/trips-all.shp")

