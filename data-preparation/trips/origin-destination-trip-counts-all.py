import pandas as pd

df = pd.read_csv("ridership-data/june2024bikeshareridership-utf8.zip", encoding="utf-8")

df['Start Station Id'] = df['Start Station Id'].fillna(0)
df['Start Station Id'] = df['Start Station Id'].astype(int, errors='ignore')
df['End Station Id'] = df['End Station Id'].fillna(0)
df['End Station Id'] = df['End Station Id'].astype(int, errors='ignore')

dfg = df.groupby(['Start Station Id', 'End Station Id']).size().reset_index(name='count')

dfg.to_csv("origin-destination-trip-counts-all.csv", index=False)