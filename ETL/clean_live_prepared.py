import pandas as pd
import os


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(base_dir, "data", "live", "zameen_live_prepared.csv")
output_path = os.path.join(base_dir, "data", "live", "zameen_live_cleaned.csv")

df = pd.read_csv(input_path)

#clean numeric
def clean_numeric(x):
    try:
        return float(str(x).replace(",","").strip())

    except:
        return None



df['price'] = df['price'].apply(clean_numeric)
df['size'] = df['size'].apply(clean_numeric)
df['bedrooms'] = pd.to_numeric(df['bedrooms'], errors = 'coerce')
df['baths'] = pd.to_numeric(df['baths'], errors = 'coerce')


# drop missing rows
df.dropna(subset = ['price', 'size','city','location'] , inplace = True)

# drop duplicates
df.drop_duplicates(inplace = True)


# Save cleaned version
df.to_csv(output_path, index=False)

print(f"✅ Cleaned live data saved to: {output_path} ({len(df)} rows)")