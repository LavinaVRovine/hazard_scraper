import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_URI

pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 50)

BASE_URL = "https://www.hltv.org"
DB_URL = f"{DATABASE_URI}csgo"
ENGINE = create_engine(DB_URL)


df = pd.read_sql_table("players_stats", ENGINE)

print()