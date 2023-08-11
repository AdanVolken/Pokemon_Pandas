import pandas as pd

datos = pd.read_csv("C:/Users/adanv/OneDrive/Escritorio/Pandas_Ptuebas/pokemon_data_gen1.csv",header=None)
datos.to_excel("C:/Users/adanv/OneDrive/Escritorio/Pandas_Ptuebas/pokemon_data_gen1.xlsx", sheet_name = "pag", engine = "openpyxl")
print(datos.head())