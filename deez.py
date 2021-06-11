import matplotlib as mpl
import pandas as pd
df = pd.read_csv('honey.csv')
df['Value'] = df['Value'].str.replace(',', '')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
df = df.dropna(subset=['Value'])
print(df['Value'])