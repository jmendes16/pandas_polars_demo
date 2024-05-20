import polars as pl
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# loading in credentials
load_dotenv()


SUPABASE_USER = os.environ.get("SUPABASE_USER")
SUPABASE_PASSWORD = os.environ.get("SUPABASE_PASSWORD")
LOCAL_USER = os.environ.get("LOCAL_USER")
LOCAL_PASSWORD = os.environ.get("LOCAL_PASSWORD")

# creating connection to raw data database
dep_conn_string = f"postgresql+psycopg2://{SUPABASE_USER}:{SUPABASE_PASSWORD}@aws-0-eu-west-2.pooler.supabase.com:5432/postgres"
dep_engine = create_engine(dep_conn_string)

# creating connection to target database/data warehouse
dest_conn_string = f"postgresql+psycopg2://{LOCAL_USER}:{LOCAL_PASSWORD}@localhost:5432/fashion_forward"
dest_engine = create_engine(dest_conn_string)

# extraction
df = pl.read_database("SELECT * FROM q3sales;", dep_engine)

# transformation
df = df.group_by('product_id').agg(pl.len().alias('count'))

# load
df.write_database('q3_product_quantities', dest_engine)