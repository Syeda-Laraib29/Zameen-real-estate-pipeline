import pandas as pd
import os

# Set paths
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(base_dir, "data", "zameen.csv")
output_path = os.path.join(base_dir, "data", "cleaned_data.csv")

# Load CSV with sep |
df = pd.read_csv(input_path, sep='|')

print("🔍 Raw data shape:", df.shape)


##########################################################

# start the cleaning

# Remove the duplicated
df.drop_duplicates(inplace = True)

# Drop the rows that are missing essential fields
df.dropna(subset=['price', 'size', 'city', 'location'], inplace=True)

#clean the numeric fields
def clean_num(val):
    if pd.isna(val):
        return None
    val = str(val).replace("PKR"," ").replace(","," ").strip()

    try:
        return float(val)
    except: 
        None

# Apply cleaning to Numeric columns

# Apply cleaning to numeric columns
df['price'] = df['price'].apply(clean_num)
df['size'] = df['size'].apply(clean_num)
df['bedrooms'] = pd.to_numeric(df['bedrooms'], errors='coerce')
df['baths'] = pd.to_numeric(df['baths'], errors='coerce')

# Now as we know that bedrooms and baths in different marls houses are almost similar then we use median to replace NaN

# Step 1-> Create size range
bins = [0, 500, 1000, 1500, 2000, 3000, 5000, 10000, float('inf')]
labels = ['0–500', '501–1000', '1001–1500', '1501–2000', '2001–3000', '3001–5000', '5001–10000', '10000+']
df['size_group'] = pd.cut(df['size'], bins=bins, labels=labels)

# Now fill NaN with median
#Bedrooms

df['bedrooms'] = df.groupby('size_group')['bedrooms'].transform(
    lambda x : x.fillna(x.median())
)

# Baths
df['baths'] = df.groupby('size_group')['baths'].transform(
    lambda x: x.fillna(x.median())
)

# Final save
df.to_csv(output_path, index=False)
print(f"✅ Cleaned data saved to: {output_path}")
print(f"✅ Final cleaned shape: {df.shape}")