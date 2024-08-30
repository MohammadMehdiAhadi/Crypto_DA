import pandas as pd
import yfinance as yf


df = yf.download("BTC-USD",interval = "1h",period = "730d")
print(df.columns)
print(df.index)


# data = yf.download("BTC-USD",interval = "1m")
#
# # df["New"] = df["Close"].rolling(window=7).min()
# print(df.shape)
# print(data.shape)
#
# # print(help(df["Close"].ewm(span=30)))
# df["Date"] = pd.to_datetime(df["Datetime"])
# df.set_index(df["Date"],inplace=True)
# print(df.index)