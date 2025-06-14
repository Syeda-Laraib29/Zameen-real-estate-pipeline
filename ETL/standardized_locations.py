import pandas as pd
import re
import os

# File paths
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(base_dir, "data", "merged", "zameen_combined.csv")
output_path = os.path.join(base_dir, "data", "merged", "zameen_combined_standardized.csv")

#load data

df = pd.read_csv(input_path)


# Clean and normalize location column
df['location_clean'] = (
    df['location']
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace(r'\s+', ' ', regex=True)
)

# Extract standardized location
def standardize_location(loc):
    if pd.isna(loc):
        return None
    base = loc.split(',')[0].strip()
    base = re.sub(r'\s+', ' ', base)
    return base.title()

df['location_standardized'] = df['location_clean'].apply(standardize_location)

# Save updated dataset
df.to_csv(output_path, index=False)
print(f"✅ Standardized location column added and saved to: {output_path}")