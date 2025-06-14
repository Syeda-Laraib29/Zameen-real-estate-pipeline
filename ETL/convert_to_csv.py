import pandas as pd 
import os

# Get path relative to the root directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(base_dir, "data", "zameen.xlsx")
output_path = os.path.join(base_dir, "data", "zameen_data_2023.csv")

# Load Excel and convert to CSV
df = pd.read_excel(input_path)
df.to_csv(output_path, index=False)

print(f"✅ Excel converted to CSV at {output_path}")