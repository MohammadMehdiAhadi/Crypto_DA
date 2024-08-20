import yfinance as yf
import pandas as pd

df = yf.download("BTC-USD",period = "2d" , interval = "15m")

# print(df)
# print("-----------------------------------------------")
# print(df.shape)
# print("-----------------------------------------------")
# print(df.columns)
df.to_csv("BTC_Price_15m.csv")