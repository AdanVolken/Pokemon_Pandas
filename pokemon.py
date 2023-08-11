import pandas as pd
from sqlalchemy import create_engine

n = 1

user = "root"
password = ""
host = "localhost"
database = "pokemon1"
table = "pokemon"
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

while n <= 9:
    ruta = f"C:/Users/adanv/OneDrive/Escritorio/Pandas_Pruebas/pokemon_data_gen{n}.csv"
    val = ruta [-1:]

    if val == "v":
        df = pd.read_csv(ruta)
        # Si la tabla no existe, se creará automáticamente con la estructura del DataFrame
        df.head(0).to_sql(table, engine, if_exists='replace', index=False)
        #df.to_sql(table, engine, if_exists='append', index=False)
    else:
        df = pd.read_excel(ruta)
        df.head(0).to_sql(table, engine, if_exists='replace', index=False)

    n += 1