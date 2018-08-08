import pandas as pd
import quandl

df = quandl.get('WIKI/PRICES')
print(df.head())
