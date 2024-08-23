import pandas as pd
import yfinance as yf


df = yf.download("BTC-USD","2022-01-01")
# df["New"] = df["Close"].rolling(window=7).min()
# print(df["New"])
print(help(df["Close"].ewm(span=30)))