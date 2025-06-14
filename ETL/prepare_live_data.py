import pandas as pd
import os

# Define file paths
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(base_dir, "data", "live", "zameen_live.csv")
output_path = os.path.join(base_dir, "data", "live", "zameen_live_prepared.csv")

# Load the raw scraped file
df = pd.read_csv(input_path, sep="|")

# Add metadata columns
df["year"] = 2025
df["source"] = "live"

# Save the updated file
df.to_csv(output_path, index=False)

print(f"✅ Updated live data saved to {output_path} with {len(df)} rows.")
