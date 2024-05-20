import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# loading in credentials
load_dotenv()

SUPABASE_USER = os.environ.get("SUPABASE_USER")
SUPABASE_PASSWORD = os.environ.get("SUPABASE_PASSWORD")

# creating connection to database
conn_string = f"postgresql+psycopg2://{SUPABASE_USER}:{SUPABASE_PASSWORD}@aws-0-eu-west-2.pooler.supabase.com:5432/postgres"
engine = create_engine(conn_string)

# extract data into a pandas dataframe
df = pd.read_sql_table('q3sales', engine)

# export data
df.to_csv('q3sales_pandas_output.csv')