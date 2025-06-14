import pandas as pd
import os

# Paths
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
hist_path = os.path.join(base_dir, "data", "cleaned_data.csv")
live_path = os.path.join(base_dir, "data", "live", "zameen_live_cleaned.csv")
output_path = os.path.join(base_dir, "data", "merged", "zameen_combined.csv")
os.makedirs(os.path.dirname(output_path), exist_ok=True)


#read csv

df_hist = pd.read_csv(hist_path)
df_live = pd.read_csv(live_path)

if 'year'  not in df_hist.columns:
    df_hist['year'] = '2023'

if 'source'  not in df_hist.columns:
    df_hist['source'] = 'historical'


# Confirm live already has year = 2025 and source = live
df_live['year'] = df_live.get('year', 2025)
df_live['source'] = df_live.get('source', 'live')


# Set column order
columns = ['city', 'location', 'price', 'bedrooms', 'baths', 'size', 'year', 'source']

df_combined = pd.concat([df_hist[columns],df_live[columns]], ignore_index = True)


df_combined.to_csv(output_path, index = False)

print(f" combined the file to :  {output_path} with total {len(df_combined)} rows")


