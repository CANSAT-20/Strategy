import pandas as pd
df = pd.read_csv('telemetrylive.csv')
df.to_excel('telemetrylive.xlsx', index=None, header=True) 