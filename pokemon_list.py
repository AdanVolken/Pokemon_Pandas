import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(f"C:/Users/adanv/OneDrive/Escritorio/Pandas_Pruebas/pokemon_list.csv")

user = "root"
password = ""
hots = "localhost"
database = "pokemon1"
table = "pokemon_list"
engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{hots}/{database}")

df.to_sql(table, engine, if_exists= "replace", index=False)