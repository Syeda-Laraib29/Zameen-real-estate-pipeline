import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
# Load cleaned and standardized dataset
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "data", "merged", "zameen_combined_standardized.csv")
df = pd.read_csv(file_path)

# DB connection settings
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# URL-encode special characters in password
from urllib.parse import quote_plus
encoded_password = quote_plus(db_password)

# Create SQLAlchemy engine
engine = create_engine(f"postgresql://{db_user}:{encoded_password}@{db_host}:{db_port}/{db_name}")

# Load to PostgreSQL (replace table if exists)
df.to_sql("properties" ,engine,   index=False, if_exists='replace')

print(f"✅ Loaded {len(df)} records into  table in {db_name} database.")
