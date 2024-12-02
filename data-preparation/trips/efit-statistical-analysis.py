import pandas as pd
import geopandas as gpd
from scipy.stats import mannwhitneyu, ks_2samp


df = pd.read_csv("ridership-data/june2024bikeshareridership-utf8.csv")

# filtered_df = df[df['Bike Model'] == "EFIT"]
# group_counts = filtered_df.groupby('Start Station Id').size()
# print(group_counts.sort_values(ascending=False))

# df = df[df['Start Station Id'] == 7001]

# print(df)


df.replace("EFIT G5", "EFIT", inplace=True)

# Rename start station and end station columns to match graphhopper data
df.rename(columns={
    'Start Station Id': 'start_id',
    'End Station Id': 'end_id'
}, inplace=True)

# Reformat all headers for consistency
df.columns = df.columns.str.lower().str.replace(' ', '_')



df_graphhopper = pd.read_csv('ridership-data/trips-graphhopper-output-all.csv')

average_df = df_graphhopper.groupby(['start_id', 'end_id']).agg({
    'distance': 'mean',
    'elevation_delta': 'mean'
}).reset_index()

# Rename the columns for clarity
average_df.rename(columns={
    'distance': 'distance_average',
    'elevation_delta': 'elevation_delta_average'
}, inplace=True)

# Merge the average_df with ridership_df on 'start_id' and 'end_id'
df = df.merge(average_df, on=['start_id', 'end_id'], how='left')




variable = "distance_average"

dfs = df.dropna(subset=[variable])

efit_group = dfs[dfs['bike_model'] == 'EFIT'][variable]
classic_group = dfs[dfs['bike_model'] == 'ICONIC'][variable]

# Perform the Mann-Whitney U test
stat, p_value = mannwhitneyu(efit_group, classic_group, alternative='two-sided')

print(f"Mann-Whitney U Statistic: {stat}")
print(f"P-value: {p_value}")

# Perform the Kolmogorov-Smirnov test
ks_stat, ks_p_value = ks_2samp(efit_group, classic_group)

print(f"Kolmogorov-Smirnov Statistic: {ks_stat}")
print(f"P-value: {ks_p_value}")