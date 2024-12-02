import pandas as pd
import geopandas as gpd

df = pd.read_csv("ridership-data/june2024bikeshareridership-utf8.csv")

# filtered_df = df[df['Bike Model'] == "EFIT"]
# group_counts = filtered_df.groupby('Start Station Id').size()
# print(group_counts.sort_values(ascending=False))

df = df[df['Start Station Id'] == 7001]

print(df)

