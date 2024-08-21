import pandas as pd
import numpy as np

df = pd.read_csv("BTC_Price_15m.csv")
df.set_index(df["Datetime"], inplace=True)

np.std()