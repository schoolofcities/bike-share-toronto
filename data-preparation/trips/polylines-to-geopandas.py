import pandas as pd
import geopandas as gpd
from shapely.geometry import LineString
import polyline
import random

def decode_polyline(encoded_polyline):

	try:
		coordinates = polyline.decode(encoded_polyline)
		coordinates = [(lon + 0.00015 * random.random() ** 2 - + 0.00015 * random.random() ** 2, lat + 0.00015 * random.random() ** 2 - + 0.00015 * random.random() ** 2) for lat, lon in coordinates]
		return LineString(coordinates)
	except:
		return None

df = pd.read_csv("ridership-data/trips-graphhopper-output-all.csv")


df['geometry'] = df['polyline_string'].apply(decode_polyline)

df = gpd.GeoDataFrame(df, geometry='geometry')

df.crs = "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs"

df.to_file("trips/trips-all.shp")

# itd be around 250mb X 7.5 so pretty big ya
# df.to_file("trips/trips-all.geojson", driver="GeoJSON")

print(df)
