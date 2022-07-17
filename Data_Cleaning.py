import pandas as pd
import numpy as np

df = pd.read_csv('IMDB_Data.csv')
del df['Unnamed: 0']

df.info()

# fill all nan cells in median
df['Movie_Metascore'].fillna(df['Movie_Metascore'].mean(), inplace=True)

df